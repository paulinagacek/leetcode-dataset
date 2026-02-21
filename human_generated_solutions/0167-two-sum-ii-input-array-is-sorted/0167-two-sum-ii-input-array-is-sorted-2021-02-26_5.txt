# Brute force - This solution did not work for me due to max time met. This will work on a simple/smaller array but not on a 1000 number array. And hence the timeout during code submission.  

class Solution(object):
    def twoSum(self, nums, target):        
        for i in range(len(nums)): # First traversal loop
            for j in range(i+1, len(nums)): # Starting 2nd loop with i+1 since numbers in the array are unique per the conditions 
                if (nums[i]+nums[j]) == target: 
                    return[i+1,j+1] # Adding 1 to each variable since the return type is 1 indexed instead of 0 indexed. 

# Using Dictionary / map - What I am doing is trying to create a dictionary such that at one point one of the numbers in nums will add upto target when added to dictionary element. If nums is [1,2,3,4,5] and target is 6, then d will become d {1:0} on first iteration and d {1:0, 2:1} on second and so on. 

class Solution:
    def twoSum(self, nums, target):
        d = {} # Defining a null dictionary which we will build with each iteration
        for i in range(len(nums)): # I found it easier and more understandable to use range instead of enumerate since this is an easy question. 
            m = target - nums[i] 
            if m in d:
                return [d[m]+1, i+1] # Adding 1 since its 1 indexed instead of default 0 indexed
            else:
                d[nums[i]] = i # Building up the dictionary


# Using 2 pointers - In this approach, I am basically taking 1st and last number of the array and adding them to see if it equals the target. If the sum is bigger than target, then I need to reduce the sum. This is only possible by reducing the last number as the array is sorted. If the sum is smaller then target, then i need to increase the sum. THis is only possible by increasing the first number as the array is sorted. I keep doing so until my lower number is less than upper number. 

class Solution:
    def twoSum(self, nums, target):
        l = 0
        r = len(nums) - 1
        while l < r:
            if nums[l] + nums[r] == target:
                return [l+1, r+1]
            if nums[l] + nums[r] > target:
                r = r - 1
            if nums[l] + nums[r] < target:
                l = l + 1