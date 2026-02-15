class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.previous_right = None
        def helper(root = root):
            if root:
                helper(root.right)
                helper(root.left)
                root.right, self.previous_right = self.previous_right, root
                root.left = None
        helper()