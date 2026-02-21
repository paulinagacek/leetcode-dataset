class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        xor_result = 0
        for x in nums:
            xor_result ^= x
            
        return xor_result