def canJump(nums):
	j = 0
	for i, x in enumerate(nums):
		if j < i: return False 
		j = max(j, i+x)
	return True