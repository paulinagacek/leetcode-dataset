def rotate(self, matrix: List[List[int]]) -> None:
	n = len(matrix)
	for row in range(math.ceil(n / 2)):
		for col in range(int(n - n / 2)):
			(
				matrix[row][col],
				matrix[~col][row],
				matrix[~row][~col],
				matrix[col][~row],
			) = (
				matrix[~col][row],
				matrix[~row][~col],
				matrix[col][~row],
				matrix[row][col],
			)
	return matrix