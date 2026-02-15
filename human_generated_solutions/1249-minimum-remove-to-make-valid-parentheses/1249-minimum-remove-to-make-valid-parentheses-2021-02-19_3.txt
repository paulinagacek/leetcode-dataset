class Solution:
    def minRemoveToMakeValid(self, S: str) -> str:
        S, stack = list(S), []
        for i, c in enumerate(S):
            if c == ")":
                if stack: stack.pop()
                else: S[i] = ""
            elif c == "(": stack.append(i)
        for i in stack: S[i] = ""
        return "".join(S)