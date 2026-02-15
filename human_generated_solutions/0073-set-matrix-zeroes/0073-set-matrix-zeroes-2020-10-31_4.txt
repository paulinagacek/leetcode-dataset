class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

        def changeRC(r,c):
            
            for col in range(len(matrix[0])):
                matrix[r][col]=\'X\' if matrix[r][col]!=0 else 0
            for row in range(len(matrix)):
                matrix[row][c]=\'X\' if matrix[row][c]!=0 else 0

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c]==0:
                    changeRC(r,c)
        
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c]==\'X\':
                    matrix[r][c]=0
                    
        #return matrix