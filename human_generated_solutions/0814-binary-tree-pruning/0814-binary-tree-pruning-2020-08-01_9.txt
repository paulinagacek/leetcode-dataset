class Solution:
    def pruneTree(self, n):
        if n:
            n.left, n.right = self.pruneTree(n.left), self.pruneTree(n.right)
            return n if any([n.val, n.left, n.right]) else None