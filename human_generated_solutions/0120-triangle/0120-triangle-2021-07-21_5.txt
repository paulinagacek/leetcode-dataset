def minimumTotal(self, triangle: List[List[int]]) -> int:
			grid = triangle
			for i in range(1, len(grid)):
				for j in range(len(grid[i])):
					if j > 0 and j < len(grid[i])-1: # aka. intermendiate node
						grid[i][j] += min(grid[i-1][j], grid[i-1][j-1])
					elif j == 0:
						grid[i][j] += grid[i-1][j]
					elif j == len(grid[i])-1:
						grid[i][j] += grid[i-1][j-1]
			# print(grid)
			return min(grid[-1])