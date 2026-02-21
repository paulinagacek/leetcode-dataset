from functools import lru_cache
class Solution:
    @lru_cache(maxsize=None)
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if s1 == s2 == s3 == \'\':
            return True
        elif s3 == \'\' and (s1 != \'\' or s2 != \'\'):
            return False
        
        if s1 == \'\':
            return s2 == s3
        elif s2 == \'\':
            return s1 == s3
       
        if s1[0] == s2[0] == s3[0]:
            return self.isInterleave(s1[1:] , s2, s3[1:]) or self.isInterleave(s1 , s2[1:], s3[1:])
        elif s1[0] == s3[0]:
            return self.isInterleave(s1[1:] , s2, s3[1:])
        elif s2[0] == s3[0]:
            return self.isInterleave(s1 , s2[1:], s3[1:])
        else:
            return False