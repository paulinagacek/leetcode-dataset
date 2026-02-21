class Solution:
    def flatten(self, root: TreeNode) -> None:
        if not root: 
            return None
        
        stack = [root]
        while len(stack):
            root = stack.pop()
            
            if root.right: 
                stack.append(root.right)
            if root.left: 
                stack.append(root.left)
                
            root.left = None
            root.right = stack[-1] if len(stack) else None