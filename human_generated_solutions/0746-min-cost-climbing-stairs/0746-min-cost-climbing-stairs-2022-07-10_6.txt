class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        
        # dp[i] represents the cost to get to the ith step
        dp = [0] * (n+1)
        
        # early exist case
        if n == 2: return min(cost[:2])
        
        # transitions
        for i in range(2, n+1):
            dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])
        
        return dp[n]