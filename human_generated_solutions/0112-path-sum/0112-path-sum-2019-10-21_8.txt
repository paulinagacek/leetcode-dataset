class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        
        sum = sum - root.val
        
        if not root.left and not root.right: #leaf node
            return sum == 0
        else:
            return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)