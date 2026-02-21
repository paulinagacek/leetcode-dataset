class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts += [0,h]
        verticalCuts += [0,w]
        
        horizontalCuts.sort()
        verticalCuts.sort()
        
        hor_diff = -1
        ver_diff = -1
        
        for i in range(1,len(horizontalCuts)):
            hor_diff = max(hor_diff,horizontalCuts[i] - horizontalCuts[i-1])
        
        for i in range(1,len(verticalCuts)):
            ver_diff = max(ver_diff,verticalCuts[i] - verticalCuts[i-1])
        
        return (hor_diff * ver_diff) % (10**9 + 7)