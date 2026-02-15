class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(n, k, 0, [], res)
        return res
    
    def dfs(self, n, k, start, path, res):
        if len(path) == k:
            res.append(path)
            return None
        
        for index in range(start, n):
            self.dfs(n, k, index+1, path+[index+1], res)
            
        
        
\'\'\'
dfs( n = 4, k = 2, start = 0, path = [], res = []) 
| index = 0
----dfs( n = 4, k = 2, start = 1, path  = [1], res = []) 
|   | index = 1
|   ----dfs ( n = 4, k = 2, start = 2, path  = [1, 2], res = [1, 2]) -> add & return
|   | index = 2
|   ----dfs( n = 4, k = 2, start = 3, path  = [1, 3], res = [[1, 2], [1, 3]]) -> add & return
|   | index = 3
|   ----dfs( n = 4, k = 2, start = 4, path  = [1, 4], res = [[1, 2], [1, 3], [1, 4]]) -> add & return
| index = 1
----dfs( n = 4, k = 2, start = 2, path  = [2], res = [[1, 2], [1, 3], [1, 4]]) 
|   | index = 2
|   ----dfs ( n = 4, k = 2, start = 3, path  = [2, 3], res = [[1, 2], [1, 3], [1, 4], [2, 3]]) -> add & return
|   | index = 3
|   ----dfs( n = 4, k = 2, start = 4, path  = [1, 4], res = [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4]]) -> add & return
| index = 2
----dfs( n = 4, k = 2, start = 3, path = [3], res = [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4]]) 
|   | index = 3
|   ----dfs ( n = 4, k = 2, start = 4, path  = [3, 4], res = [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]) -> add & return
| index = 3
----dfs( n = 4, k = 2, start = 4, path = [4], res = [[1, 2], [1, 3], [1, 4], [2, 3], [3, 4]]) -> return None
\'\'\'