class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        ans = [None] * len(nums)
        n = len(nums)
        bestBitIndices = [0] * 32

        for numIndex in range(len(nums) - 1, -1, -1):
            
            for bitIndex in range(32):
                if nums[numIndex] & (1 << bitIndex):
				    # if 0 we need to atleast travel till the current index
                    if bestBitIndices[bitIndex] == 0:
                        bestBitIndices[bitIndex] = numIndex
                    else:
                        bestBitIndices[bitIndex] = min(bestBitIndices[bitIndex], numIndex)
                    
            ans[numIndex] = max(1, max(bestBitIndices) - numIndex + 1)
        
        return ans