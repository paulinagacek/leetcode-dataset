class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = 0
        for i in range(len(accounts)):
            max_wealth = max(sum(accounts[i]), max_wealth)
        
        return max_wealth