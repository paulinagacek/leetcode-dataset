class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        else:
            left = self.rightSideView(root.left)
            right = self.rightSideView(root.right)
            if len(right) >= len(left):
                return [root.val] + right
            else:
                return [root.val] + right + left[len(right):]