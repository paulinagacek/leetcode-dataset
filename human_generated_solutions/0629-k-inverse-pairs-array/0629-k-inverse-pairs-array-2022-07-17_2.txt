class Solution:
    def kInversePairs(self, n: int, k: int) -> int:

        dp, mod = [1]+[0] * k, 1_000_000_007
        
        for i in range(n):
            tmp, sm = [], 0

            for j in range(k + 1):
                sm+= dp[j]
                if j-i >= 1: sm-= dp[j-i-1]
                sm%= mod
                tmp.append(sm)

            dp = tmp

            #print(dp)       # <-- uncomment this line to get a sense of dp from the print output
			                 #     try n = 6, k = 4; your answer should be 49.
        return dp[k]