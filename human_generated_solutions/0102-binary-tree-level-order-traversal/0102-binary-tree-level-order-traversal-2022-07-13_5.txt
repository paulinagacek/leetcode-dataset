class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        
        def dfs(node, depth):
            if not node:
                return
            if depth >= len(ans):
                ans.append([])
            ans[depth].append(node.val)
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)
        
        dfs(root, 0)
        return ans