class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix: return 0
        m, n = len(matrix), len(matrix[0])
        if not n: return 0
		
        r, r1, r2 = -1, 0, m-1
        while r1 <= r2:
            mid = (r1+r2) // 2 
            if matrix[mid][0] <= target <= matrix[mid][n-1]: r = mid; break
            elif matrix[mid][0] > target: r2 = mid - 1
            else: r1 = mid + 1    
        if r == -1: return False        
        
        c1, c2 = 0, n-1
        while c1 <= c2:
            mid = (c1+c2) // 2 
            if matrix[r][mid] == target: return True
            elif matrix[r][mid] > target: c2 = mid - 1
            else: c1 = mid + 1
        return False