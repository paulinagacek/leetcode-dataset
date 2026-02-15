def combine(self, n: int, k: int) -> List[List[int]]:
	res = []
	# seen = set() # -- we cannot use sum becuz 2+3 = 1+4
	nums = list(range(1, n+1))
	stack = [([], nums[::-1])]
	while stack:
		combo, nums = stack.pop()
		if len(combo) == k: # or if nums = n - k
			if sorted(combo) not in res:
				res.append(combo)

		for i in range(len(nums)):
			if len(combo) >= k:
				continue
			newNums = nums[:i] + nums[i+1:]
			newCombo = combo + [nums[i]]
			stack.append((newCombo, newNums))
	return res