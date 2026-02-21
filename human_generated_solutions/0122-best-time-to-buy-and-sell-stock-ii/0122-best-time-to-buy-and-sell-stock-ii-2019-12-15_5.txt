class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        arr=[0 for i in range(len(prices))]
        for i in range(len(prices)-1):
            arr[i+1]=prices[i+1]-prices[i]
        
        maxProfit=0
        for i in range(len(arr)):
            if arr[i]>0:
                maxProfit+=arr[i]
        return maxProfit