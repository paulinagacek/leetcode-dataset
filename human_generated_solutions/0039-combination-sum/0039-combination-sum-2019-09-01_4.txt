class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # return self.combinationSumRecurisve(candidates, target, [])
        return self.combinationSumDP(candidates, target)
    
    def combinationSumDP(self, candidates, target):
        dp = {}
        dp[0] = [[]]
        candidates.sort()
        for c in candidates:
            for t in range(c, target + 1):
                if (t-c) in dp:
                    if t not in dp:
                        dp[t] = []
                    for comb_t_m_c in dp[t-c]:
                        dp[t].append(comb_t_m_c + [c])
        return dp[target] if target in dp else []
        
    
    def combinationSumRecurisve(self, candidates, target, curr_nums):
        if target == 0:
            return [curr_nums]
        
        if len(candidates) == 0 or target <= 0:
            return []
        
        c = candidates[0]
        sol = self.combinationSumRecurisve(candidates[1:], target, curr_nums)
        sol.extend(self.combinationSumRecurisve(candidates, target - c, curr_nums + [c]))
        return sol