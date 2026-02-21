class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        if not root:
            return True
        
        queue = [root.left, root.right]
        
        while len(queue) > 0:
            # pop 2 from queue
            left = queue.pop(0)
            right = queue.pop(0)
            
            # Evalate the pair
            if not left and not right:
                continue
            elif left and right and left.val == right.val:
                pass
            else:
                return False
            
            # Enqueue children
            queue.append(left.left)
            queue.append(right.right)
            queue.append(left.right)
            queue.append(right.left)
        
        return True