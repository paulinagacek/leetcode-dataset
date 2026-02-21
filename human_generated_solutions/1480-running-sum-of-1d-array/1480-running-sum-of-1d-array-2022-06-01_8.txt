class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        return [tot := nums[0]] + [tot := i+tot for i in nums[1:]]