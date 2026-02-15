class Solution:
    def findFinalValue(self, n: List[int], o: int) -> int:
        n = sorted(n)
        for i in range(len(n)) :
            if o == n[i]:
                o *= 2
        return o