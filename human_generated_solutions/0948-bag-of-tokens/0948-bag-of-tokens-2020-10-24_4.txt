class Solution:
    def bagOfTokensScore(self, tokens: List[int], P: int) -> int:
        tokens.sort()
        low, high = 0, len(tokens)-1
        score, max_score = 0, 0
        while low <= high:
            if tokens[low] <= P:
                P-=tokens[low]
                score+=1
                max_score = max(score, max_score)
                low+=1
            elif score >= 1:
                P+=tokens[high]
                score-=1
                high-=1
            else:
                break
        return max_score