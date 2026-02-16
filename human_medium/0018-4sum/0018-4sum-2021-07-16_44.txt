class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        
        hashMap = {}
        output = []
        
        ## Create dictionary of complements
        
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                
                if nums[i] + nums[j] not in hashMap:
                    hashMap[nums[i]+nums[j]] = [[i, j, nums[i], nums[j]]]
                else:
                    hashMap[nums[i]+nums[j]].append([i, j, nums[i], nums[j]])
    
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                
                complement = target - (nums[i]+nums[j])
                
                if complement in hashMap:
                    
                    for item in hashMap[complement]:
                        ## Now see that there are no overlapping indexes
                        if i != item[0] and j != item[0] and j != item[1] and i != item[1]:
                            
                            temp = [nums[i], nums[j], item[2], item[3]]
                            temp.sort()
                            if temp not in output:
                                output.append(temp)
        return output
