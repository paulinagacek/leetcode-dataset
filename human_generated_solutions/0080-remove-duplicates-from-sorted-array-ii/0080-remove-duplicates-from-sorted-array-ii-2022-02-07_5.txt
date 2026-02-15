class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length = len(nums)
        if len(nums) < 2:
            return length
        i = 0
        while(i <=  length-1):
            count = nums.count(nums[i])
            if count > 2:
                for _ in range(i,i+count-2):
                    nums.pop(i)
                i += 2
                length -= (count-2)
            else:
                i += 1