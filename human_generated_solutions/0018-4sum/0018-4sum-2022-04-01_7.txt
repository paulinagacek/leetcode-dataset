class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans = set()
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                # two sum problem solution
                new_target = target - (nums[i] + nums[j])
                start = j+1
                end = n-1
                while end > start:
                    if(nums[start] + nums[end] == new_target):
                        ans.add((nums[i], nums[j], nums[start], nums[end]))
                        end -= 1
                        start += 1
                    elif nums[start] + nums[end] > new_target:
                        end -= 1
                    else:
                        start += 1
        return ans