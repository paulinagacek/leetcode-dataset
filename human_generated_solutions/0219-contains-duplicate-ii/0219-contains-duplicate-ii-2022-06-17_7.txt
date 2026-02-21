class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
	# when we see a num present in d, we check (if the current index - the index of d[num] ) <= k, 
	# we return True, otherwise loop goes on and the duplicate key\'s value gets updated with current index
	# and ofcourse we return False.
        d = {}
        for i, num in enumerate(nums):
            if num in d and i - d[num] <= k: # similar to (j - i) <= k, where the i==j(cur idx) and d[num] holds i
                return True
            d[num] = i
        return False