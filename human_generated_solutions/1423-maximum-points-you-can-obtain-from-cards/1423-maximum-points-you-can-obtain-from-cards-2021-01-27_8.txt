class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        sumup = sum(cardPoints[:k])
        res = sumup
       
        for i in range(k):
            sumup+= -cardPoints[k-i-1] + cardPoints[-i-1]
            res = max(res, sumup)
        
        return res