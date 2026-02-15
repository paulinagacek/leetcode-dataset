def iterative(self, root):
        # this solutions is faster than 99.65% \uD83D\uDE32
        if not root: return root
        stack = [root]
        while len(stack):
            node = stack.pop()
            node.left, node.right = node.right, node.left
            if node.left: stack.append(node.left)
            if node.right: stack.append(node.right)
        return root
        
    def recursive(self, root):
        def rec(root):
            if root:
                root.left, root.right = root.right, root.left
                rec(root.left)
                rec(root.right)
        rec(root)
        return root