class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        
        if k >= len(s):
            return s[::-1]
        
        i = 0
        s = list(s)
        while i < len(s):
            l = i
            h = (i + k - 1) if (i + k - 1) < len(s) else len(s) - 1
            while l < len(s) and l < h:
                s[l], s[h] = s[h], s[l]
                l += 1
                h -= 1
            i += (2 * k)
        return "".join(s)