class Solution:
	"""
	Time:   O(n*m*log(max(n,m))
	Memory: O(n*m)
	"""

	def diagonalSort(self, matrix: List[List[int]]) -> List[List[int]]:
		n, m = len(matrix), len(matrix[0])
		diags = defaultdict(list)

		for i in range(n):
			for j in range(m):
				diags[i - j].append(matrix[i][j])

		for k in diags:
			diags[k].sort(reverse=True)

		for i in range(n):
			for j in range(m):
				matrix[i][j] = diags[i - j].pop()

		return matrix