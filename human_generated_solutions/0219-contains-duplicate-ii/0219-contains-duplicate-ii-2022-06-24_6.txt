class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l = set()
        for i in range(len(nums)):
            if len(l) >= k+1:
                l.remove(nums[i-k-1]) # remove left-most elem
            if nums[i] in l:
                return True
            l.add(nums[i])
        return False