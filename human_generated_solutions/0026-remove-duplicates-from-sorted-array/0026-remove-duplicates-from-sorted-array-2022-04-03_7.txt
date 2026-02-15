class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        check = 0
        for i in range(1, len(nums)):
            if nums[check] != nums[i]:
                check+=1
                nums[check] = nums[i]
        return check+1