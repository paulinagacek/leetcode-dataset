class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return sorted(nums + [target]).index(target)