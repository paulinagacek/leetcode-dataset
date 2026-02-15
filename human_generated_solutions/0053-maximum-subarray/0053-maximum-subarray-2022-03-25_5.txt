class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
	
        local_max = -pow(10, 4)         # as per provided constraints
        global_max = -pow(10, 4)        # as per provided constraints
        
        for i in range(len(nums)):
            local_max = max(nums[i], nums[i] + local_max)
            if local_max > global_max:
                global_max = local_max
        
        return global_max