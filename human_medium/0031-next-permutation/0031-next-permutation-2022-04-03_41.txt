class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        last_peak_idx = -1
        i = len(nums) - 1
        # Identify the index of last peak.
        while i > 0:
            if nums[i] > nums[i - 1]:
                last_peak_idx = i
                break
            i -= 1

        # Case a: If the given input is in descending order.
        if last_peak_idx == -1:
            nums.sort()
            return

        idx, i = last_peak_idx, last_peak_idx
        # case b: If the given input is not in descending order.
        while i < len(nums):
            if nums[last_peak_idx - 1] < nums[i] < nums[idx]:
                # Special Case: Find an smallest element which exists between nums[lastPeakIdx-1] and nums [lastPeakIdx]
                idx = i
            i += 1

        nums[idx], nums[last_peak_idx - 1] = nums[last_peak_idx - 1], nums[idx]
        nums[last_peak_idx:] = sorted(nums[last_peak_idx:])
