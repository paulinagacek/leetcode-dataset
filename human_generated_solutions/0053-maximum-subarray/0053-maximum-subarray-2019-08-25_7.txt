class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0]*len(nums)
        dp[0] = nums[0]
        """
        dp[1] = max(dp[0]+nums[1],nums[1])
        dp[2] = max(dp[1]+nums[2],nums[2])
        """
        for i in range(1,len(nums)):
            dp[i] = max(dp[i-1] +nums[i],nums[i])
        return max(dp)