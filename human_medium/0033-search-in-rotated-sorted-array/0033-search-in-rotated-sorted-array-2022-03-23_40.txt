class Solution:
    def search(self, nums: List[int], target: int) -> int:
        N = len(nums)
        left, right = 0, N - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if nums[mid] == target:
                return mid
            
            # base case 1: sorted array
            if nums[left] < nums[right]: 
                if nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
            
            # base case 2: rotated array
            else: 
                if nums[mid] >= nums[right]:
                    if nums[left] <= target < nums[mid]:
                        right =  mid - 1
                    else:
                        left = mid + 1
                elif nums[mid] < nums[right]:
                    if nums[mid] < target <= nums[right]:
                        left = mid + 1
                    else:
                        right = mid - 1
                
        return -1
