class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!=len(t) or len(set(s))!=len(set(t)):
            return False
        hashmap={}
        
        for i in range(len(s)):
            if s[i] not in hashmap:
                hashmap[s[i]]=t[i]
            
            if hashmap[s[i]]!=t[i]:
                return False
        return True