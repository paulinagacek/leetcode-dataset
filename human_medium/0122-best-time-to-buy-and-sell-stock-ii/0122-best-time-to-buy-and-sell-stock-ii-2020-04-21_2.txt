class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1: # edge case
            return 0
        
        # take down positive daily return only
        profit = [] 
        for i in range(1, len(prices)):
            profit.append(max(0, prices[i] - prices[i-1])) 
        return sum(profit)
