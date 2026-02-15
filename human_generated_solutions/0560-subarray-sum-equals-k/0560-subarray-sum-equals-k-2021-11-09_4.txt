class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        currentSum = 0
        subarrays = 0
        hashmap = {}
        for num in nums:
            currentSum += num
            if currentSum == k:
                subarrays += 1
            if currentSum - k in hashmap:
                subarrays += hashmap[currentSum-k]
            if currentSum in hashmap:
                hashmap[currentSum] += 1
            else:
                hashmap[currentSum] = 1
        return subarrays