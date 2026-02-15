def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
	cache = [[] for _ in range(target + 1)]
	cache[0] = [[]]
	for c in candidates:
		for i in range(target + 1):
			if i >= c:
				for temp_ans in cache[i - c]:
					cache[i].append(temp_ans + [c])
	return cache[-1]