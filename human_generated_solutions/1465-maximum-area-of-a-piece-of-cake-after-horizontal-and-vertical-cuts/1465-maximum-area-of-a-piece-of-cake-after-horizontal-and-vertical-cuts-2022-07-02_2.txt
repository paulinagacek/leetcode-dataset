class Solution:
    def calcMaxDist(self, cuts, end):
        cuts.append(0)
        cuts.append(end)
        cuts.sort()
        return max(cuts[i] - cuts[i - 1] for i in range(1, len(cuts)))
        
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        MOD = 10 ** 9 + 7
        maxWidth = self.calcMaxDist(horizontalCuts, h)
        maxHeight = self.calcMaxDist(verticalCuts, w)
        return (maxWidth * maxHeight) % MOD