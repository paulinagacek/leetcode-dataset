class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ranges = []
        
        start = None        
        for i, n in enumerate(nums):
            if start is None:
                start = n
            if i == len(nums) - 1 or n < nums[i + 1] - 1:
                ranges.append(str(start) + "->" + str(n) if start != n else str(n))                
                start = None
            
        return ranges