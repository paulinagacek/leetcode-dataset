class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        total = 0 
        for i, x in enumerate(mat):
            if i == len(mat)-i-1:
                total += x[i]
            else: 
                total += x[i] + x[len(mat)-i-1]
        return total