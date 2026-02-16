class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        r = -(k % len(nums))
        if len(nums[:r]): nums[:r], nums[r:] = nums[r:], nums[:r]
        else: nums[r:], nums[:r] = nums[:r], nums[r:]
