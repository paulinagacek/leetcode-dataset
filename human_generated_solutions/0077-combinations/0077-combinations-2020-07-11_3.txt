def combine(self, n, k):
    res = [] #1
    self.dfs(range(1,n+1), k, 0, [], res) #2
    return res #3
    
def dfs(self, nums, k, index, path, res):  #4
	print(\'index is:\', index)
    print(\'path is:\', path)
    if k == 0:  #7
        res.append(path)  #8
        return # backtracking  #9 
    for i in range(index, len(nums)):  #10
        self.dfs(nums, k-1, i+1, path+[nums[i]], res)  #11