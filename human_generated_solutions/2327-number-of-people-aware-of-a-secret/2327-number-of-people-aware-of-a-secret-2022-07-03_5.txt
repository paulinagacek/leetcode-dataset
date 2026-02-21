class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        
        dp = [0]*(n+1)
        
        for i in range(1, n+1):
            dp[i] += 1
            for k in range(i+delay, i+forget):
                if k < n+ 1:
                    dp[k] += dp[i]
            if i+forget < n+1:
                dp[i+forget] -= 1
                
        return dp[-1] % (10**9+7)