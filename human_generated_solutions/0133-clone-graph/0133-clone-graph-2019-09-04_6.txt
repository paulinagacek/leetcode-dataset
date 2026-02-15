class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if node == None:
            return None
        
        self.visited = dict()
        node_copy = Node(node.val, [])
        self.visited[node] = node_copy
        self.dfs(node)
        return node_copy
    
    def dfs(self, node):
        for neighbor in node.neighbors:
            if neighbor not in self.visited:    # add the neighbor node to visited dict
                neighbor_copy = Node(neighbor.val, [])
                self.visited[neighbor] = neighbor_copy
                self.visited[node].neighbors.append(neighbor_copy)
                self.dfs(neighbor)
            else:   # use the neighbor node in the visited dict
                self.visited[node].neighbors.append(self.visited[neighbor])