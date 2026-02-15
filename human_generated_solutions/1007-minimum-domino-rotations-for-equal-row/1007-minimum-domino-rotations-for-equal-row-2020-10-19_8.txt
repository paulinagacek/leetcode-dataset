from collections import Counter
class Solution(object):
    def minDominoRotations(self, A, B):
        n = len(A)
        
        a = Counter(A)
        m1 = max(a.items(), key = lambda x: x[1])
        k1 = m1[0]
        v1 = m1[1]
        
        x1 = n - v1
        y1 = x1
        for i in range(n):
            if A[i] != k1:
                if B[i] == k1:
                    x1 -= 1
        
        
        
        b = Counter(B)
        m2 = max(b.items(), key = lambda x: x[1])
        k2 = m2[0]
        v2 = m2[1]
        
        x2 = n - v2
        y2 = x2
        for i in range(n):
            if B[i] != k2:
                if A[i] == k2:
                    x2 -= 1
        
        if x1 != 0 and x2 != 0:
            return -1
        return min(y1, y2)