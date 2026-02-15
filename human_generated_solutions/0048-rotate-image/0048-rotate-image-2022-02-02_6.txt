class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        rLen, cLen = len(matrix), len(matrix[0])
        
        #Transposing
        for r in range(rLen):
            for c in range(cLen):
                if r > c:
                    matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]

        #Folding
        for r in range(rLen):
            for c in range(cLen):
                center = cLen // 2
                if c < center:
                    matrix[r][c], matrix[r][cLen - c - 1] = matrix[r][cLen - c - 1], matrix[r][c]
        
        return matrix