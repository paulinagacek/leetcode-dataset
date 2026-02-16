class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = nums[0]
        max_ = min_ = 1
        for n in nums:
            max_, min_ = max(n, n * max_, n * min_), min(n, n * max_, n * min_)
            result = max(result, max_)
            
        return result
