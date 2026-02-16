class Solution(object):
    def cloneGraph(self, node):
        if not node:
            return

        copy_map = {}

        def dfs(node):
            if node in copy_map:  # visited
                return copy_map[node]

            copy_map[node] = Node(node.val, [])  # base case

            for nei in node.neighbors:
                copy_map[node].neighbors.append(dfs(nei))

            return copy_map[node]

        return dfs(node)
