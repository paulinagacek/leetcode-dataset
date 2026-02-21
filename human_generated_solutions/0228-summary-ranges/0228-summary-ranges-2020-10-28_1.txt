class Solution:
    def getStr(self, first, last):
        return str(first) if first == last else f"{first}->{last}"

    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return nums
        
        res = []
        first = nums[0]
        for i in range(1, len(nums)):
            if nums[i-1]+1 != nums[i]:
                res.append(self.getStr(first, nums[i-1]))
                first = nums[i]
                
        res.append(self.getStr(first, nums[-1]))
        return res