class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        ## RC ##
        ## APPROACH : DFS ##
        
		## TIME COMPLEXITY : O(N) ##
		## SPACE COMPLEXITY : O(N) ##

        def dfs(node, path, total):
            if not node:   return
            if(total + node.val == sum and not node.left and not node.right):       # watchout for conditions
                result.append(path + [node.val])
                return
            if(node.left):  dfs(node.left, path + [node.val], total + node.val)
            if(node.right): dfs(node.right, path + [node.val], total + node.val)
        result = []
        dfs(root, [], 0)
        return result