class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        buckets = {0:0, 1:0, 2:0}
        for num in nums:
            buckets[num] += 1
        
        last_index = 0
        for val, count in buckets.items():
            current_index = last_index + count
            nums[last_index:current_index] = [val] * (current_index - last_index)
            last_index = current_index
        
        return nums
