class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        s=0
        n=len(nums)
        m=len(multipliers)
        dp=[[0]*(m+1) for i in range(m+1)]
        for j in range(m-1, -1, -1):
            for low in range(j, -1, -1):
                first=nums[low]*multipliers[j]+dp[j+1][low+1]
                last=nums[n-1-(j-low)]*multipliers[j]+dp[j+1][low]
                dp[j][low]=max(first, last)
        return dp[0][0]