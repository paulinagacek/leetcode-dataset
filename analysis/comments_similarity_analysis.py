import os
import tokenize
from io import StringIO
import numpy as np
import matplotlib.pyplot as plt
from itertools import combinations, product
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

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

BASE_DIR_HUMAN = "human_medium"
BASE_DIR_AI = "ai_medium"


# =====================================================
# Comment Extraction
# =====================================================

def remove_task_header(code):
    if "class Solution" in code:
        return code.split("class Solution", 1)[1]
    return code


def extract_comments(code):
    code = remove_task_header(code)
    comments = []

    try:
        tokens = tokenize.generate_tokens(StringIO(code).readline)
        for toknum, tokval, _, _, _ in tokens:
            if toknum == tokenize.COMMENT:
                cleaned = tokval.lstrip("#").strip()
                if len(cleaned) > 2:
                    comments.append(cleaned)
    except Exception:
        pass

    return " ".join(comments)


# =====================================================
# Similarity Computation
# =====================================================

def compute_comment_similarity(texts):
    if len(texts) < 2:
        return np.array([])

    vectorizer = TfidfVectorizer(stop_words="english")
    tfidf = vectorizer.fit_transform(texts)

    sim_matrix = cosine_similarity(tfidf)

    sims = []
    n = sim_matrix.shape[0]
    for i in range(n):
        for j in range(i + 1, n):
            sims.append(sim_matrix[i, j])

    return np.array(sims)


def compute_cross_similarity(texts_a, texts_b):
    if not texts_a or not texts_b:
        return np.array([])

    vectorizer = TfidfVectorizer(stop_words="english")
    tfidf = vectorizer.fit_transform(texts_a + texts_b)

    n_a = len(texts_a)
    tfidf_a = tfidf[:n_a]
    tfidf_b = tfidf[n_a:]

    sim_matrix = cosine_similarity(tfidf_a, tfidf_b)

    return sim_matrix.flatten()


# =====================================================
# Dataset Collection
# =====================================================

def collect_comment_data():

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

                comments = extract_comments(code)

                if not comments.strip():
                    continue

                if group_type:
                    task_data[task][group_type].append(comments)
                else:
                    if f.startswith("gpt"):
                        task_data[task]["gpt"].append(comments)
                    elif f.startswith("gemini"):
                        task_data[task]["gemini"].append(comments)

    collect(BASE_DIR_HUMAN, "human")
    collect(BASE_DIR_AI)

    return task_data


# =====================================================
# Aggregated Similarities
# =====================================================

def aggregate_similarities(task_data):

    results = {
        "human": [],
        "gpt": [],
        "gemini": [],
        "human_gpt": [],
        "human_gemini": [],
    }

    for task, groups in task_data.items():

        # Intra
        results["human"].extend(compute_comment_similarity(groups["human"]))
        results["gpt"].extend(compute_comment_similarity(groups["gpt"]))
        results["gemini"].extend(compute_comment_similarity(groups["gemini"]))

        # Cross
        results["human_gpt"].extend(
            compute_cross_similarity(groups["human"], groups["gpt"])
        )
        results["human_gemini"].extend(
            compute_cross_similarity(groups["human"], groups["gemini"])
        )

    for k in results:
        results[k] = np.array(results[k])

    return results


# =====================================================
# Plotting
# =====================================================

def plot_distribution(values, title, filename):

    if len(values) == 0:
        print(f"No data for {title}")
        return

    plt.figure(figsize=(10, 7))
    plt.hist(values, bins=50, alpha=0.7, color="steelblue", edgecolor="black")

    lower = np.percentile(values, 5)
    upper = np.percentile(values, 95)

    plt.axvline(lower, linestyle="--")
    plt.axvline(upper, linestyle="--")
    plt.axvspan(lower, upper, alpha=0.15)

    plt.xlabel("Comment Similarity (Cosine)")
    plt.ylabel("Pairwise Frequency")
    plt.xlim(0, 1)
    plt.title(title)
    plt.tight_layout()
    plt.savefig(filename, dpi=300)
    plt.close()

    print(f"Saved: {filename}")

# =====================================================
# Comment Similarity Statistics
# =====================================================

def print_comment_statistics(values, name):

    values = np.array(values)

    if len(values) == 0:
        print(f"\n{name}: No data available.")
        return

    mean_val = np.mean(values)
    median_val = np.median(values)
    p5 = np.percentile(values, 5)
    p95 = np.percentile(values, 95)

    pct_above_60 = np.mean(values > 0.60) * 100
    pct_above_80 = np.mean(values > 0.80) * 100
    pct_above_90 = np.mean(values > 0.90) * 100
    pct_equal_100 = np.mean(values == 1.00) * 100

    print(f"\n=== {name} ===")
    print(f"Total pairs: {len(values)}")
    print(f"Mean similarity: {mean_val:.4f}")
    print(f"Median similarity: {median_val:.4f}")
    print(f"5–95% interval: [{p5:.4f}, {p95:.4f}]")
    print(f"% > 0.60 : {pct_above_60:.2f}%")
    print(f"% > 0.80 : {pct_above_80:.2f}%")
    print(f"% > 0.90 : {pct_above_90:.2f}%")
    print(f"% = 1.00 : {pct_equal_100:.2f}%")


# =====================================================
# Main
# =====================================================

if __name__ == "__main__":

    task_data = collect_comment_data()
    results = aggregate_similarities(task_data)

    # -------------------------
    # Print Statistics
    # -------------------------

    print_comment_statistics(results["human"], "Comment Similarity: Human vs Human")
    print_comment_statistics(results["gpt"], "Comment Similarity: GPT vs GPT")
    print_comment_statistics(results["gemini"], "Comment Similarity: Gemini vs Gemini")
    print_comment_statistics(results["human_gpt"], "Comment Similarity: Human vs GPT")
    print_comment_statistics(results["human_gemini"], "Comment Similarity: Human vs Gemini")

    # -------------------------
    # Plot Distributions
    # -------------------------

    plot_distribution(
        results["human"],
        "Comment Similarity: Human vs Human",
        "comment_similarity_human_intra.png",
    )

    plot_distribution(
        results["gpt"],
        "Comment Similarity: GPT vs GPT",
        "comment_similarity_gpt_intra.png",
    )

    plot_distribution(
        results["gemini"],
        "Comment Similarity: Gemini vs Gemini",
        "comment_similarity_gemini_intra.png",
    )

    plot_distribution(
        results["human_gpt"],
        "Comment Similarity: Human vs GPT",
        "comment_similarity_human_gpt.png",
    )

    plot_distribution(
        results["human_gemini"],
        "Comment Similarity: Human vs Gemini",
        "comment_similarity_human_gemini.png",
    )