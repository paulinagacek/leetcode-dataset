class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        while l < r:
            m = (l+r)//2
            if nums[l] < nums[r]:
                return nums[l]
            else:
                if l+1 == r:
                    return nums[r]
                elif nums[l] < nums[m] and nums[m] > nums[r]:
                    l = m+1
                else: 
                    r = m
        return nums[l]