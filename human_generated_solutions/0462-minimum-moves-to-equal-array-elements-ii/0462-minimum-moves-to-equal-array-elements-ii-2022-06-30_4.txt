from statistics import median as m
class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        x = int(m(nums))
        return sum([abs(i-x) for i in nums])