def iterative(self, root):
        if not root:
            return 0
        stack = [[root, 1]]
        h = 0
        m = 0
        while len(stack):
            top, h = stack.pop()
            if top.left: stack.append([top.left, h + 1])
            if top.right: stack.append([top.right, h + 1])
            m = max(h, m)
        return m