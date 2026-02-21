class Solution:
    def canJump(self, nums: List[int]) -> bool:
        N = len(nums)
    
        def dfs(i):
            if i == N - 1:
                return True
            
            if nums[i] == 0:
                return False
            
            for j in range(i + 1, min(i + nums[i], N - 1) + 1):
                if dfs(j):
                    return True
            
            return False
        
        return dfs(0)