class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        # store nums in memory
        memory = set(nums)
        # explore the chains of consecutive numbers in the array
        current_max = 1
        for e in nums:
            # is it the begining of the chain
            if e - 1 in memory: continue
            counter = 1
            while e + 1 in memory:
                counter += 1
                e += 1
            # update max
            current_max = max(current_max, counter)
        return current_max
