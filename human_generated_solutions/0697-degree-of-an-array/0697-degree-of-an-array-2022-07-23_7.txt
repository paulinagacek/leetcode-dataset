class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        dict_ = {}
        l=len(nums)
        for i in range(l):
            if nums[i] in dict_:
                dict_[nums[i]][0]+=1
                dict_[nums[i]][2]=i-dict_[nums[i]][1] #updating difference between first and last idx
            else:
                dict_[nums[i]] = [1,i,0] #count, first idx, difference between first and last idx
                
        max_c=0 
        for i in dict_:
            max_c = max(max_c,dict_[i][0]) #getting max occurence
        #print(max_c)
        nums_max_c = []
        for i in dict_:
            if dict_[i][0] == max_c:
                nums_max_c.append(i) #getting numbers with max occurence
        #print(nums_max_c)
        
        min_dist=51000
        for i in nums_max_c:
            min_dist = min(min_dist,dict_[i][2]) #getting min distance between first and last idx among selected numbers
        return min_dist+1