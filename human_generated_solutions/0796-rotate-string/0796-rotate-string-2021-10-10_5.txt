class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        for i in range(len(s) + 1):
            if s[i:] + s[:i] == goal:
                return True
        return False