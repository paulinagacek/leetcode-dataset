import os
import ast
import math
import numpy as np
from collections import Counter
from itertools import combinations, product


# =====================================================
# Identifier Extraction
# =====================================================

class IdentifierExtractor(ast.NodeVisitor):
    """
    Extract user-defined identifiers:
    - Variable assignments
    - Function parameters
    - Loop variables
    """

    def __init__(self):
        self.identifiers = []

    def visit_Name(self, node):
        if isinstance(node.ctx, ast.Store):
            self.identifiers.append(node.id)
        self.generic_visit(node)

    def visit_arg(self, node):
        self.identifiers.append(node.arg)

    def visit_FunctionDef(self, node):
        # Include function name itself
        self.identifiers.append(node.name)
        self.generic_visit(node)


def extract_identifiers(code):
    try:
        tree = ast.parse(code)
    except SyntaxError:
        return []

    extractor = IdentifierExtractor()
    extractor.visit(tree)
    return extractor.identifiers


# =====================================================
# Shannon Entropy
# =====================================================

def compute_entropy(identifier_list):
    """
    H(p) = - sum Prob(id) * log2 Prob(id)
    """
    if not identifier_list:
        return 0.0

    counts = Counter(identifier_list)
    total = len(identifier_list)

    entropy = 0.0
    for count in counts.values():
        p = count / total
        entropy -= p * math.log2(p)

    return entropy


# =====================================================
# Jaccard Similarity
# =====================================================

def jaccard_similarity(set1, set2):
    if not set1 or not set2:
        return 0.0
    return len(set1 & set2) / len(set1 | set2)


# =====================================================
# Dataset Processing
# =====================================================

def collect_identifiers(human_dir, ai_dir):
    """
    Returns:
        task_data[task] = {
            "human": [set_of_ids, ...],
            "gpt": [...],
            "gemini": [...]
        }
    """

    task_data = {}

    def process_directory(base_dir, group=None):
        for task in os.listdir(base_dir):
            task_path = os.path.join(base_dir, task)
            if not os.path.isdir(task_path):
                continue

            if task not in task_data:
                task_data[task] = {"human": [], "gpt": [], "gemini": []}

            for fname in os.listdir(task_path):
                file_path = os.path.join(task_path, fname)

                with open(file_path, "r", encoding="utf-8") as f:
                    code = f.read()

                identifiers = extract_identifiers(code)
                id_set = set(identifiers)

                if group:
                    task_data[task][group].append((identifiers, id_set))
                else:
                    if fname.startswith("gpt"):
                        task_data[task]["gpt"].append((identifiers, id_set))
                    elif fname.startswith("gemini"):
                        task_data[task]["gemini"].append((identifiers, id_set))

    process_directory(human_dir, group="human")
    process_directory(ai_dir)

    return task_data


# =====================================================
# Entropy Analysis
# =====================================================

def compute_entropy_stats(task_data):

    results = {}

    for group in ["human", "gpt", "gemini", "ai_combined"]:
        entropies = []

        for task, groups in task_data.items():

            if group == "ai_combined":
                reps = groups["gpt"] + groups["gemini"]
            else:
                reps = groups[group]

            for identifiers, _ in reps:
                entropies.append(compute_entropy(identifiers))

        entropies = np.array(entropies)

        results[group] = {
            "mean_entropy": np.mean(entropies),
            "median_entropy": np.median(entropies),
            "std_entropy": np.std(entropies),
        }

    return results


# =====================================================
# Cross-Solution Identifier Jaccard
# =====================================================

def compute_identifier_jaccard(task_data, group_a, group_b=None):
    """
    If group_b is None → intra-group
    Else → cross-group
    """

    similarities = []

    for task, groups in task_data.items():

        if group_b is None:
            reps = groups[group_a]
            pairs = combinations(reps, 2)
        else:
            reps_a = groups[group_a]
            reps_b = groups[group_b]
            pairs = product(reps_a, reps_b)

        for (_, set1), (_, set2) in pairs:
            similarities.append(jaccard_similarity(set1, set2))

    similarities = np.array(similarities)

    return {
        "mean": np.mean(similarities),
        "median": np.median(similarities),
        "p95": np.percentile(similarities, 95),
        "pct_gt_06": np.mean(similarities > 0.6) * 100,
        "pct_gt_09": np.mean(similarities > 0.9) * 100,
    }

def compute_human_vs_ai(task_data):
    """
    Cross-group similarity: Human vs (GPT + Gemini combined)
    """

    similarities = []

    for task, groups in task_data.items():

        humans = groups["human"]
        ai = groups["gpt"] + groups["gemini"]

        if not humans or not ai:
            continue

        for (_, set_h), (_, set_ai) in product(humans, ai):
            similarities.append(jaccard_similarity(set_h, set_ai))

    similarities = np.array(similarities)

    return {
        "mean": np.mean(similarities),
        "median": np.median(similarities),
        "p95": np.percentile(similarities, 95),
        "pct_gt_06": np.mean(similarities > 0.6) * 100,
        "pct_gt_09": np.mean(similarities > 0.9) * 100,
    }


# =====================================================
# Main Execution
# =====================================================

if __name__ == "__main__":

    human_dir = "human_medium"
    ai_dir = "ai_medium"

    task_data = collect_identifiers(human_dir, ai_dir)

    # ---- Entropy ----
    entropy_results = compute_entropy_stats(task_data)

    print("\n=== Identifier Entropy ===")
    for group, stats in entropy_results.items():
        print(f"\n{group.upper()}")
        print(f"Mean Entropy: {stats['mean_entropy']:.4f}")
        print(f"Median Entropy: {stats['median_entropy']:.4f}")
        print(f"Std Entropy: {stats['std_entropy']:.4f}")

    # ---- Jaccard ----
    print("\n=== Identifier Jaccard Similarity ===")

    # Cross comparisons
    human_gpt = compute_identifier_jaccard(task_data, "human", "gpt")
    human_gemini = compute_identifier_jaccard(task_data, "human", "gemini")
    human_ai = compute_human_vs_ai(task_data)

    print("\nHUMAN vs GPT")
    for k, v in human_gpt.items():
        print(f"{k}: {v:.4f}")

    print("\nHUMAN vs GEMINI")
    for k, v in human_gemini.items():
        print(f"{k}: {v:.4f}")

    print("\nHUMAN vs AI (Combined)")
    for k, v in human_ai.items():
        print(f"{k}: {v:.4f}")