class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left = 0
        right = n - 1
        while left <= right:
            mid = (left + right) // 2
            left_val = nums[left]
            mid_val = nums[mid]
            if mid_val == target:
                return mid
            
            elif ((left_val < mid_val and left_val <= target < mid_val) or
                  (left_val > mid_val and (target < mid_val or target >= left_val))):
                  
                right = mid - 1
                  
            else:
                left = mid + 1
        return -1
