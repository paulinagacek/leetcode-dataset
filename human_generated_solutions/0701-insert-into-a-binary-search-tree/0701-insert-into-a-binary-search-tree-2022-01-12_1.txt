class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root: return TreeNode(val)
            
        cur, next = None, root
        while next:
            cur = next
            next = cur.left if val < cur.val else cur.right
        
        if val < cur.val: 
            cur.left = TreeNode(val)
        else: 
            cur.right = TreeNode(val)
            
        return root