class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        if k==0 or n<1:
            return res
        
        self.dfs(n, k, [], res, 1)
        return res
        
    def dfs(self, n, k, path, res, index):
        length = len(path)
        #if len(path) == k:
        if length == k:
            res.append(path[:])
            return
        
        # TLE problem solved by adding this
        if k-length > n - index + 1: # need k numbers in total , still need (k-lenth)
            return
        
        for num in range(index, n+1):
            if num not in path:
                path += [num]        
                self.dfs(n, k, path, res, num+1)
                path.pop()