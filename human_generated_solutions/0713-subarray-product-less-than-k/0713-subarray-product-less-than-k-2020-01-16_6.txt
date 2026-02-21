class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        
        if k <= 1:
            # Quick response for invalid k on product of positive numbers
            return 0
        
        else:
            left_sentry = 0

            num_of_subarray = 0
            product_of_subarry = 1

            # update right bound of sliding window
            for right_sentry in range( len(nums) ):

                product_of_subarry *= nums[right_sentry]

                # update left bound of sliding window
                while product_of_subarry >= k:
                    product_of_subarry //= nums[left_sentry]
                    left_sentry += 1

                # Note:
                # window size = right_sentry - left_sentry + 1

                # update number of subarrary with product < k
                num_of_subarray += right_sentry - left_sentry + 1

            return num_of_subarray