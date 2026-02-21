class Solution:
    def rightSideView(self, root: TreeNode) -> list[int]:
        ans =[]
        
        def dfs(node =root,level=1):
            if not node: return
            
            if len(ans) < level: 
                ans.append(node.val)
            dfs(node.right,level+1)         #  <--- right first
            dfs(node.left ,level+1)         #  <--- then left

            return 

        dfs()
        return ans