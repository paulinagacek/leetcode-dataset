class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        lenP, i, j, s = len(pushed), 0, 0, 0
        while i < lenP:
            if ~s and popped[j] == pushed[s]:
                j += 1
                s -= 1
            else:
                s += 1
                i += 1
                if i < lenP: pushed[s] = pushed[i]
        return not s