class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = " ".join(s.split())
        return 0 if len(s)==0 else len(s.split(" ")[-1])