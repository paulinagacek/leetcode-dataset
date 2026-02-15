class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        if len(nums) >= 3:
            checked = set()
            count = 0
            nums.sort()
            for i in range(len(nums) - 1, -1, -1):
                if nums[i] not in checked and count == 2:
                    return nums[i]
                elif nums[i] not in checked:
                    checked.add(nums[i])
                    count += 1
            return max(nums)
        else:
            return max(nums)