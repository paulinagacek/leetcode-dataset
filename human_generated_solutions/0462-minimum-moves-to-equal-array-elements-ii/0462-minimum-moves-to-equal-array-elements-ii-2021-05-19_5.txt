class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        
        for i in range(len(nums)):
            ans += abs(nums[i] - nums[len(nums) // 2])
        
        return ans