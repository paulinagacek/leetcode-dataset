import os
import ast
import hashlib
import numpy as np
from itertools import combinations, product
import matplotlib.pyplot as plt

plt.rcParams.update(
    {
        "font.size": 14,
        "axes.titlesize": 14,
        "axes.labelsize": 14,
        "xtick.labelsize": 14,
        "ytick.labelsize": 14,
        "legend.fontsize": 14,
    }
)

# =====================================================
# AST Normalization
# =====================================================


class ASTNormalizer(ast.NodeTransformer):
    def visit_Name(self, node):
        return ast.copy_location(ast.Name(id="VAR", ctx=node.ctx), node)

    def visit_Constant(self, node):
        return ast.copy_location(ast.Constant(value="CONST"), node)

    def visit_arg(self, node):
        node.arg = "VAR"
        return node


# =====================================================
# Subtree Hashing
# =====================================================


def hash_string(s):
    return hashlib.sha256(s.encode()).hexdigest()


def compute_subtree_hash(node):
    child_hashes = []
    all_hashes = set()

    for child in ast.iter_child_nodes(node):
        child_hash, child_subtrees = compute_subtree_hash(child)
        child_hashes.append(child_hash)
        all_hashes.update(child_subtrees)

    label = type(node).__name__
    combined = label + "(" + ",".join(child_hashes) + ")"
    node_hash = hash_string(combined)

    all_hashes.add(node_hash)

    return node_hash, all_hashes


def get_subtree_hashes(code):
    try:
        tree = ast.parse(code)
    except SyntaxError:
        return None

    normalizer = ASTNormalizer()
    tree = normalizer.visit(tree)
    ast.fix_missing_locations(tree)

    _, subtree_hashes = compute_subtree_hash(tree)
    return subtree_hashes


# =====================================================
# Similarity
# =====================================================


def jaccard_similarity(set1, set2):
    if not set1 or not set2:
        return 0
    return len(set1 & set2) / len(set1 | set2)


# =====================================================
# Dataset-Level Analysis
# =====================================================


def analyze_structural_similarity(human_dir, ai_dir):

    task_data = {}

    def collect(path, group_type=None):
        for task in os.listdir(path):
            t_path = os.path.join(path, task)
            if not os.path.isdir(t_path):
                continue

            if task not in task_data:
                task_data[task] = {"human": [], "gpt": [], "gemini": []}

            for f in os.listdir(t_path):
                file_path = os.path.join(t_path, f)

                with open(file_path, "r", encoding="utf-8") as file:
                    code = file.read()

                subtree_hashes = get_subtree_hashes(code)
                if subtree_hashes is None:
                    continue

                if group_type:
                    task_data[task][group_type].append(subtree_hashes)
                else:
                    if f.startswith("gpt"):
                        task_data[task]["gpt"].append(subtree_hashes)
                    elif f.startswith("gemini"):
                        task_data[task]["gemini"].append(subtree_hashes)

    collect(human_dir, "human")
    collect(ai_dir)

    results = {}

    for group in ["human", "gpt", "gemini", "ai_combined"]:

        all_pairwise = []
        task_means = []
        task_stds = []

        for task, groups in task_data.items():

            if group == "ai_combined":
                reps = groups["gpt"] + groups["gemini"]
            else:
                reps = groups[group]

            if len(reps) < 2:
                continue

            sims = []
            for r1, r2 in combinations(reps, 2):
                sims.append(jaccard_similarity(r1, r2))

            sims = np.array(sims)

            all_pairwise.extend(sims)
            task_means.append(np.mean(sims))
            task_stds.append(np.std(sims))

        results[group] = {
            "all_pairwise": np.array(all_pairwise),
            "task_means": np.array(task_means),
            "task_stds": np.array(task_stds),
        }

    return results, task_data


# =====================================================
# Cross-Group Similarity
# =====================================================


def compute_cross_group_similarity(task_data, group_a, group_b):

    all_pairwise = []
    task_means = []
    task_stds = []

    for task, groups in task_data.items():

        reps_a = groups[group_a]
        reps_b = groups[group_b]

        if not reps_a or not reps_b:
            continue

        sims = []

        for r1, r2 in product(reps_a, reps_b):
            sims.append(jaccard_similarity(r1, r2))

        sims = np.array(sims)

        all_pairwise.extend(sims)
        task_means.append(np.mean(sims))
        task_stds.append(np.std(sims))

    return {
        "all_pairwise": np.array(all_pairwise),
        "task_means": np.array(task_means),
        "task_stds": np.array(task_stds),
    }

def compute_human_vs_ai(task_data):

    all_pairwise = []
    task_means = []
    task_stds = []

    for task, groups in task_data.items():

        humans = groups["human"]
        ai = groups["gpt"] + groups["gemini"]

        if not humans or not ai:
            continue

        sims = []

        for h, a in product(humans, ai):
            sims.append(jaccard_similarity(h, a))

        sims = np.array(sims)

        all_pairwise.extend(sims)
        task_means.append(np.mean(sims))
        task_stds.append(np.std(sims))

    return {
        "all_pairwise": np.array(all_pairwise),
        "task_means": np.array(task_means),
        "task_stds": np.array(task_stds),
    }



# =====================================================
# Plotting
# =====================================================


def plot_structural_distribution(
    data, title, filename, out_dir
):

    os.makedirs(out_dir, exist_ok=True)

    fig, ax1 = plt.subplots(figsize=(10, 7))

    # Global pairwise similarity histogram
    counts, bins, patches = ax1.hist(
        data["all_pairwise"],
        bins=50,
        alpha=0.7,
        color="steelblue",
        edgecolor="black"
    )

    ax1.set_xlabel("Structural Similarity")
    ax1.set_ylabel("Pairwise Frequency")
    ax1.set_xlim(0, 1)

    # Set axis colors to black
    ax1.tick_params(axis="both", colors="black")
    ax1.spines["top"].set_color("black")
    ax1.spines["right"].set_color("black")
    ax1.spines["left"].set_color("black")
    ax1.spines["bottom"].set_color("black")

    # 90% central interval (5th–95th percentile)
    lower = np.percentile(data["all_pairwise"], 5)
    upper = np.percentile(data["all_pairwise"], 95)

    ax1.axvline(lower, color="black", linestyle="--", linewidth=1.5)
    ax1.axvline(upper, color="black", linestyle="--", linewidth=1.5)
    ax1.axvspan(lower, upper, color="gray", alpha=0.15)

    range_text = f"90% Interval\n[{lower:.3f}, {upper:.3f}]"

    ax1.text(
        0.02,
        0.90,
        range_text,
        transform=ax1.transAxes,
        fontsize=13,
        verticalalignment="top",
        bbox=dict(boxstyle="round", facecolor="white", alpha=0.85),
    )

    plt.title(title)
    plt.tight_layout()
    plt.savefig(os.path.join(out_dir, filename), dpi=300)
    plt.close()

    print(f"Saved: {filename}")

def plot_human_vs_models_overlay(human_gpt, human_gemini, title, filename, out_dir):

    os.makedirs(out_dir, exist_ok=True)

    fig, ax = plt.subplots(figsize=(10, 7))

    # Extract similarity arrays
    gpt_vals = human_gpt["all_pairwise"]
    gemini_vals = human_gemini["all_pairwise"]

    # Plot histograms
    ax.hist(
        gpt_vals,
        bins=50,
        alpha=0.6,
        color="steelblue",
        label="Human–GPT",
    )

    ax.hist(
        gemini_vals,
        bins=50,
        alpha=0.5,
        color="darkorange",
        label="Human–Gemini",
    )

    # Compute 5th and 95th percentiles
    gpt_p5 = np.percentile(gpt_vals, 5)
    gpt_p95 = np.percentile(gpt_vals, 95)

    gemini_p5 = np.percentile(gemini_vals, 5)
    gemini_p95 = np.percentile(gemini_vals, 95)

    # Draw percentile lines
    ax.axvline(gpt_p5, color="steelblue", linestyle="--", linewidth=2)
    ax.axvline(gpt_p95, color="steelblue", linestyle="--", linewidth=2)

    ax.axvline(gemini_p5, color="darkorange", linestyle="--", linewidth=2)
    ax.axvline(gemini_p95, color="darkorange", linestyle="--", linewidth=2)

    # Optional shaded 90% central region (lighter)
    ax.axvspan(gpt_p5, gpt_p95, color="steelblue", alpha=0.08)
    ax.axvspan(gemini_p5, gemini_p95, color="darkorange", alpha=0.08)

    # Annotate interval values
    ylim = ax.get_ylim()[1]

    ax.text(
        gpt_p95 + 0.01,
        ylim * 0.95,
        f"GPT 5–95%: [{gpt_p5:.3f}, {gpt_p95:.3f}]",
        color="steelblue",
        rotation=90,
        verticalalignment="top",
    )

    ax.text(
        gemini_p95 + 0.01,
        ylim * 0.75,
        f"Gemini 5–95%: [{gemini_p5:.3f}, {gemini_p95:.3f}]",
        color="darkorange",
        rotation=90,
        verticalalignment="top",
    )

    ax.set_xlabel("Structural Similarity")
    ax.set_ylabel("Pairwise Frequency")
    ax.set_xlim(0, 1)

    ax.legend()
    plt.title(title)
    plt.tight_layout()
    plt.savefig(os.path.join(out_dir, filename), dpi=300)
    plt.close()

    print(f"Saved: {filename}")

# =====================================================
# Distribution Summary Statistics
# =====================================================

def print_similarity_statistics(values, name):

    values = np.array(values)

    if len(values) == 0:
        print(f"\n{name}: No data available.")
        return

    pct_above_60 = np.mean(values > 0.60) * 100
    pct_above_90 = np.mean(values > 0.90) * 100
    pct_above_95 = np.mean(values > 0.95) * 100
    pct_equal_100 = np.mean(values == 1.00) * 100

    print(f"\n=== {name} ===")
    print(f"Total pairs: {len(values)}")
    print(f"% > 0.60 : {pct_above_60:.2f}%")
    print(f"% > 0.90 : {pct_above_90:.2f}%")
    print(f"% > 0.95 : {pct_above_95:.2f}%")
    print(f"% = 1.00 : {pct_equal_100:.2f}%")

# =====================================================
# Usage
# =====================================================

if __name__ == "__main__":

    results, task_data = analyze_structural_similarity(
        "human_medium", "ai_medium"
    )

    # -------------------------
    # Print Intra-group Statistics
    # -------------------------

    print_similarity_statistics(results["human"]["all_pairwise"], "Human vs Human (Intra)")
    print_similarity_statistics(results["gpt"]["all_pairwise"], "GPT vs GPT (Intra)")
    print_similarity_statistics(results["gemini"]["all_pairwise"], "Gemini vs Gemini (Intra)")

    # -------------------------
    # Intra-group plots
    # -------------------------

    plot_structural_distribution(
        results["human"],
        "Intra-group Structural Similarity: Human vs Human",
        "structural/structural_similarity_human_intra.png",
        "plots",
    )

    plot_structural_distribution(
        results["gpt"],
        "Intra-group Structural Similarity: GPT vs GPT",
        "structural/structural_similarity_gpt_intra.png",
        "plots",
    )

    plot_structural_distribution(
        results["gemini"],
        "Intra-group Structural Similarity: Gemini vs Gemini",
        "structural/structural_similarity_gemini_intra.png",
        "plots",
    )

    # -------------------------
    # Cross-group plots
    # -------------------------

    human_gpt = compute_cross_group_similarity(task_data, "human", "gpt")
    human_gemini = compute_cross_group_similarity(task_data, "human", "gemini")
    human_ai = compute_human_vs_ai(task_data)

    plot_human_vs_models_overlay(
        human_gpt,
        human_gemini,
        "Cross-Group Structural Similarity: Human vs GPT and Gemini",
        "structural/structural_similarity_human_vs_models.png",
        "plots",
    )

    print_similarity_statistics(human_gpt["all_pairwise"], "Human vs GPT")
    print_similarity_statistics(human_gemini["all_pairwise"], "Human vs Gemini")
    print_similarity_statistics(human_ai["all_pairwise"], "Human vs AI (Combined)")