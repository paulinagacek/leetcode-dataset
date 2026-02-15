"""
SOLUTION:
https://leetcode.com/discuss/general-discussion/1078072/introduction-to-topological-sort

# indegree = count of incoming edges of each vertex/node or how many parents it has (used to determine sources)
# source: Any node that has no incoming edge and has only outgoing edges is called a source (indegree==0)

- top_sort = []
- get the topological sort of the courses
    - initialization:
        - create an adjacency list from the edge list given
        - while doing so, create an indegree record for each vertex/node
        - add all the sources into a queue
    - while queue:
        - get the element at the top of the queue (curr)
            - add it to the output
            - reduce the indegree for all of its children by one
                - if any child has an indegree of one after that, add it to the queue
                
- return len(top_sort) == len(adjacency_list)
    - if len(top_sort) == len(adjacency_list), it means the graph is acyclic
"""




import collections


class Solution:
    def topSort(self, edge_list):
        top_sort = []

        # # create an adjacency list from the edge list given
        # while doing so, create an indegree record for each vertex/node
        adjacency_list = collections.defaultdict(list)
        indegrees = collections.defaultdict(int)
        for arr in edge_list:
            child, parent = arr[0], arr[1]

            adjacency_list[parent].append(child)
            indegrees[child] += 1

        # # add all the sources into a queue
        queue = []
        for vertex in adjacency_list:
            if indegrees[vertex] == 0:
                queue.append(vertex)

        # # build top_sort list
        while queue:
            vertex = queue.pop(0)
            top_sort.append(vertex)
            for child in adjacency_list[vertex]:
                indegrees[child] -= 1
                if indegrees[child] == 0:
                    queue.append(child)

        # if len(top_sort) == len(adjacency_list), it means the graph is acyclic
        return len(top_sort) == len(adjacency_list)

    def canFinish(self, numCourses, prerequisites):
        return self.topSort(prerequisites)