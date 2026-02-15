# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def inOrder(root, low, high, ans):
            if not root:
                return
            if root.val >= low and root.val <= high:
                ans.append(root.val)
            inOrder(root.left, low, high, ans)
            inOrder(root.right, low, high, ans)
            return sum(ans)
        return inOrder(root, low, high, [])