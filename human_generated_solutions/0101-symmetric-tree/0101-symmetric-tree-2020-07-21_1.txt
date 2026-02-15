class Solution:
    def isSymmetric(self, root):
        stack = []
        if root: stack.append([root.left, root.right])

        while(len(stack) > 0):
            left, right = stack.pop()
            
            if left and right:
                if left.val != right.val: return False
                stack.append([left.left, right.right])
                stack.append([right.left, left.right])
        
            elif left or right: return False
        
        return True