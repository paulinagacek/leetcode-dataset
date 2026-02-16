class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        all_combinations = list(combinations(range(1,10), k))
        sum_n = [c for c in all_combinations if sum(c)==n]
        return sum_n
