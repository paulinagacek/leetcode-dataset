class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        
        
        
        x = "".join(sorted(map(str,nums),cmp=lambda a,b: 1 if a+b>b+a else -1 if b+a>a+b else 0,reverse=True))
        
        return "0" if x.count("0") == len(x) else x
