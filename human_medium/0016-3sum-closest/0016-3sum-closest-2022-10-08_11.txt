class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        
        result = sum(nums[:3])
        for i in range(len(nums)-2):
            if i==0 and nums[i] == nums[i-1]:
                continue
            
            l, r = i+1, len(nums)-1
            while l < r:
                curr = nums[i] + nums[l] + nums[r]
                diff = curr - target
                if diff < 0:
                    l += 1
                elif diff > 0:
                    r -= 1
                else:
                    return curr
                """
                TLE for block if statement
                
                if abs(result-target) > abs(diff):
                    result = curr
                """
                result = curr if abs(result-target) > abs(diff) else result

        
        return result
