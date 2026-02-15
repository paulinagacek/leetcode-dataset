class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(cur_res, start, remaining_target):
            if 0 == remaining_target:
                res.append(cur_res)
                return
            for i in range(start, len(candidates)):
                num = candidates[i]
                if num > remaining_target:
                    continue
                dfs(cur_res + [num], i, remaining_target - num)
        
        dfs([], 0, target)
        return res