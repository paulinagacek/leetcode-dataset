from collections import deque

class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        mod = 10 ** 9  + 7
        # day 1
        q, sharing, pre = deque([1] + [0] * (forget - 1)), 0, delay - 1
        
        for _ in range(1, n):
            sharing += q[pre] - q.pop() 
            q.appendleft(sharing % mod)
        
        return sum(q) % mod