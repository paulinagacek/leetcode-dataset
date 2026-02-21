class Solution(object):
    def levelOrder(self, root):
        from collections import deque
        deque, ret = deque(), []
        if root:
            deque.append(root)
        while deque:
            level, size = [], len(deque)
            for _ in range(size):
                node = deque.popleft()
                level.append(node.val)
                if node.left:
                    deque.append(node.left)
                if node.right:
                    deque.append(node.right)
            ret.append(level)
        return ret
		
    def levelOrder(self, root):
        res = []
        self.dfs(root, 0, res)
        return res
        
    def dfs(self, root, level, res):
        if not root:
            return 
        if len(res) < level+1:
            res.append([])
        res[level].append(root.val)
        self.dfs(root.left, level+1, res)
        self.dfs(root.right, level+1, res)