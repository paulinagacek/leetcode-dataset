def containsNearbyDuplicate(nums, k):  # update a dictionary once you see a duplicate and make a decision
	if len(nums) <= 1: return False  # no duplicates
    if len(set(nums)) == len(nums): return False  # no duplicates
    d = {}
    for i, n in enumerate(nums):
        if n not in d:
            d[n] = i
        else:
            idx_diff = abs(i - d[n])
            if idx_diff <= k:
                return True
            else: 
				d[n] = i
    return False