class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        ans = []
        def helper(candidates, target, t):
            if not target:
                ans.append(t)
                return
            for i, num in enumerate(candidates):
                if target >= num:
                    helper(candidates[i:], target - num, t + [num])
                else: break
        helper(candidates, target, [])
        return ans