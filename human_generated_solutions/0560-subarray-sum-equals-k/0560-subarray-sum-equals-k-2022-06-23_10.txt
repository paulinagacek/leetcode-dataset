class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        i = 0
        j = 0
        n = len(nums)
        s = 0
        subarrayCount = 0
        while j < n:
            s += nums[j]
            if s < k:
                j += 1
            elif s == k:
                subarrayCount += 1
                j += 1
            else:
                while s > k:
                    s -= nums[i]
                    i += 1
                    if s == k:
                        subarrayCount += 1
                        break
                    j += 1
        return subarrayCount