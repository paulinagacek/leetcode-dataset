class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        bit = {}
        N = len(nums)
        for i in range(1,32):
            bit[i] = 0
        last = 0
        ans = 0
        for first in range(N):
            flag = True
            currE = nums[first]
            for j in range(1,32):
                if currE & 1<<(j-1):
                    bit[j] += 1
                    if bit[j] > 1:
                        flag = False
            if flag:
                ans = max(ans,first-last+1)
            else:
                while True:
                    nxt = nums[last]
                    if last > N:
                        break
                    last += 1
                    for j in range(1,32):
                        if nxt & 1<<(j-1):
                            bit[j] -=1
                    f = True
                    for j in range(1,32):
                        if bit[j] > 1:
                            f = False
                            break
                    if f:
                        break
                    
        return ans