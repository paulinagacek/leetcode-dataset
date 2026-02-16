class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # create graph
        graph = [[] for _ in range(numCourses)]
        for pre in prerequisites:
            graph[pre[0]].append(pre[1])
          
        ans = []
        seen = [0 for _ in range(numCourses)]
        
        # dfs
        def topSort(node, graph, seen, ans):
            if (seen[node] != 0): return seen[node]
            seen[node] = -1 # mark as seen
            for neigh in graph[node]:
                if(topSort(neigh, graph, seen, ans)==-1):
                    return -1
            ans.append(node)
            seen[node] = 1 # done without cycle
            return 0
        
        for i in range(numCourses):
            if (seen[i] == 0): 
                if (topSort(i, graph, seen, ans)==-1): # cycle
                    return []
        return ans
