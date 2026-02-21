class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascal_triangle = [[1 for _ in range(row + 1)] for row in range(numRows)]
        
        for row in range(numRows):
            for col in range(1, row):
                pascal_triangle[row][col] = pascal_triangle[row - 1][col] + pascal_triangle[row - 1][col - 1]
        
        return pascal_triangle