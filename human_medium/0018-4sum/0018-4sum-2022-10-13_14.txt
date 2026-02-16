class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        for a in range(0, len(nums) - 3):
            if (a > 0 and nums[a] == nums[a - 1]):continue

            for d in range(len(nums) - 1, -1, -1):
                if (d < len(nums) - 1 and nums[d] == nums[d + 1]):continue

                b,c = a + 1,d - 1
                while(b < c):
                    pair = nums[a] + nums[b] + nums[c] + nums[d]
                    if (pair > target):
                        c -= 1
                    elif(pair < target):
                        b += 1
                    
                    else:
                        res.append([nums[a],nums[b], nums[c], nums[d]])
                        b += 1
                        while (nums[b] == nums[b - 1] and b < c):
                            b += 1
        
        return res
