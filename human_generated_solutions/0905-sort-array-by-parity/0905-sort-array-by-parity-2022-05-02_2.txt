class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for i in nums:
            if i%2 == 0:
                res.insert(0, i)
            else:
                res.append(i)
        return res