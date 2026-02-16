def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prev_max = nums[0] # max from previous iteration
        prev_min = nums[0] # min from previous iteration
        max_to_n = nums[0] # max this iteration
        min_to_n = nums[0] # min this iteration
        ans = nums[0]
        
        for i in nums[1:]
			# use previous max/min*current i or restart from i. The absolute value of the min could be larger so we store it.
			max_to_n = max(max(prev_max*i, prev_min*i), i)
            min_to_n = min(min(prev_max*i, prev_min*i), i)
            prev_max = max_to_n
            prev_min = min_to_n
            ans = max(ans, max_to_n)
        return ans
