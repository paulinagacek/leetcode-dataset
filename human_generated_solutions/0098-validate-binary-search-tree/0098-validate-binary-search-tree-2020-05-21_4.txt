def iterative(self, root):
        if not root: return True
        stack = [(root, -float(\'inf\'), float(\'inf\'))]
        while len(stack):
            node, left, right = stack.pop()
            if node.val <= left or node.val >= right: return False
            if node.left: stack.append((node.left, left, node.val))
            if node.right: stack.append((node.right, node.val, right))
        return True
        
        
        
        
    def recursive(self, root): 
        def rec(node, left, right):
            if node:
                if node.val <= left or node.val >= right: return False
                return rec(node.left, left, node.val) and rec(node.right, node.val, right)
            return True
        return rec(root, -float(\'inf\'), float(\'inf\') )