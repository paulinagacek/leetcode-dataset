class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        strings = []
        for i in range(0,len(A[0])):
            temp = "".join([item[i] for item in A])
            if "".join(sorted(temp)) == temp:
                pass
            else:
                strings.append(1)
        return len(strings)