def rightSideView(self, root: TreeNode) -> List[int]:
        # Step 1: identify the end of the level
        # Step 2: add last node to the result
        
        # dfs
        # 1) prioritize right side
        # 2) keep track level of nodes
        
        res = []
        self.dfs(root, 0, res)
        return res
    
    def dfs(self, node, curLevel, res):
        if not node: #base case to return
            return
        
        if curLevel >= len(res): #push the value in
            res.append(node.val)
            
        #preorder traversal
        if node.right:
            self.dfs(node.right, curLevel+1, res)
        if node.left:
            self.dfs(node.left, curLevel+1, res)
# T: O(N)
# S: O(N)