class Solution:
    def minimumLength(self, s: str) -> int:
        i,j=0,len(s)-1
        while i<j and s[i]==s[j]:
            t=s[i]
            while i<len(s) and s[i]==t:
                i+=1
            while j>=0 and s[j]==t:
                j-=1
        if j<i:
            return 0
        return j-i+1