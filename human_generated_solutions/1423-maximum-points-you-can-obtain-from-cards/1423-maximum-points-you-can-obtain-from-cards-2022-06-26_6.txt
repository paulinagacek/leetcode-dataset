class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        length = len(cardPoints)
        s = sum(cardPoints[-k:])
        maximum = s
        j = length-k
        i=0
        while i!=j and j<length:
            s+=cardPoints[i]
            s-=cardPoints[j]
            i+=1
            j+=1
            maximum = max(s,maximum)
        return maximum