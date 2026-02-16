class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(i) for i in nums]
        maxi = max(nums,key=lambda x:len(x))
        max_len = len(maxi)
        nums = sorted(nums, key = lambda x:str(x * (10*(max_len-len(x) + 1))),reverse = True)       
        res = "".join(nums)
        res = int(res)//1
        return str(res)
