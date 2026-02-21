class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        windowStart = 0
        hashmap = {x: 0 for x in nums}
        max_length = 0
        if 0 not in hashmap.keys():
            return len(nums) - 1
        for windowEnd in range(len(nums)):
            hashmap[nums[windowEnd]] += 1
            if hashmap[0] > 1:
                hashmap[nums[windowStart]] -= 1
                windowStart += 1
            
            max_length = max(max_length, windowEnd - windowStart)
        return (max_length)