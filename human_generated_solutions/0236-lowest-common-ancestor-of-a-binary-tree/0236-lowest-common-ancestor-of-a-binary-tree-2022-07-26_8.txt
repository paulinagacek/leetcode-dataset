class RecursionOutput:
    def __init__(self, q_found: bool, p_found: bool, lowest_common_ancestor: \'TreeNode\' = None):
        self.q_found = q_found
        self.p_found = p_found
        self.lowest_common_ancestor = lowest_common_ancestor

class Solution:
    def lowestCommonAncestor(self, root: \'TreeNode\', p: \'TreeNode\', q: \'TreeNode\') -> \'TreeNode\':
        
        def search(node: \'TreeNode\'):
            if not node: return RecursionOutput(False, False)
            
            # Initial values
            is_q_found = False
            is_p_found = False
            
            # Search on left side
            left_output = search(node.left)
            
            # Already found LCA on left side -> short circuit return
            if left_output.lowest_common_ancestor is not None:
                return left_output
            
            # Search on right side
            right_output = search(node.right)
            
            # Found LCA on right side -> short circuit return
            if right_output.lowest_common_ancestor is not None:
                return right_output
            
            # Check if we found q in either left or right side
            if left_output.q_found or right_output.q_found:
                is_q_found = True
            
			 # Check if we found p in either left or right side
            if left_output.p_found or right_output.p_found:
                is_p_found = True
            
            
            # Check if current node is either q or p
            if node == q:
                is_q_found = True
            if node == p:
                is_p_found = True
             
            # Prepare the output
            output = RecursionOutput(is_q_found, is_p_found)
            
            # if found LCA
            if is_q_found and is_p_found:
                output.lowest_common_ancestor = node
            
            return output
                
        
        search_result = search(root)
        return search_result.lowest_common_ancestor