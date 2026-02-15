class Solution:
    def minCostClimbingStairs(self, c: List[int]) -> int:
    	c1, c2 = c[0], c[1]
    	for i in range(2,len(c)): c1, c2 = c2, c[i] + min(c1,c2)
    	return min(c1, c2)