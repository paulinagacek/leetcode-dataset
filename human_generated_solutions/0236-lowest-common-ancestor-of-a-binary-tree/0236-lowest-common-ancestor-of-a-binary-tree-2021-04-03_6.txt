def lowestCommonAncestor(self, root: \'TreeNode\', p: \'TreeNode\', q: \'TreeNode\') -> \'TreeNode\':
        
        def dfs(node):
            if node in (None, p, q):
                return node
            
            llca, rlca = dfs(node.left), dfs(node.right)
            return node if llca and rlca else llca or rlca
        
        return dfs(root)