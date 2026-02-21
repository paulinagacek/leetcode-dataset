def searchMatrix(self, A: List[List[int]], target: int) -> bool:
	n, m = len(A), len(A[0])
	l = bisect_left(range(m * n - 1), target, key= lambda x: A[x // m][x % m])
	return A[l // m][l % m] == target