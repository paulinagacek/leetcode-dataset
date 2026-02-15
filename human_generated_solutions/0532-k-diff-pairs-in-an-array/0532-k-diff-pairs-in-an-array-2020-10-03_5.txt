class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        d = {}
        cnt = 0
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        
        if k == 0:
            for i in d.values():
                if i > 1:
                    cnt += 1
        else:
            for i in d:
                if k + i in d:
                    cnt += 1
            
        return cnt