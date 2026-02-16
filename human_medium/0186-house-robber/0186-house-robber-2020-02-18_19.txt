class Solution:
    def rob(self, nums: List[int]) -> int:
        
        size = len(nums)
        value_dp = [ 0 for _ in range(size) ]
        
        if size == 0:
            # Empty list
            return 0
        
        elif size == 1:
            # Only one item
            return nums[0]
    
        else:
            # Initialization
            value_dp[0] = nums[0]
            value_dp[1] = max(nums[0], nums[1])

            # General case
            for i in range(2, size):
                value_dp[i] = max(value_dp[i-2] + nums[i], value_dp[i-1] )

            return value_dp[-1]
