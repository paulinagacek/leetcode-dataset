class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:

        d = defaultdict(int)                                # d keeps track of most recent index of num (if seen)

                                                            #  Ex:  nums = [1,2,3,1,6,0,2],  k = 5
                                                            #                               num in d and
        for i, num in enumerate(nums):                      #   i   num         d             i - j <= 5
                                                            #  \u2013\u2013\u2013  \u2013\u2013\u2013 \u2013\u2013\u2013\u2013\u2013\u2013\u2013\u2013\u2013\u2013\u2013\u2013\u2013\u2013\u2013\u2013\u2013\u2013 \u2013\u2013\u2013\u2013\u2013\u2013\u2013\u2013\u2013\u2013\u2013\u2013\u2013\u2013\u2013\u2013\u2013 
            if num in d and i - d[num] <= k: return True    #   0    1   {}                     False
                                                            #   1    2   {1: 0}                 False
            d[num] = i                                      #   2    3   {1: 0, 2: 1})          False
                                                            #   3    1   {1: 0, 2: 1, 3: 2}     True    <= 3 - 0 <5
        return False                                        #   |            |                             |   |