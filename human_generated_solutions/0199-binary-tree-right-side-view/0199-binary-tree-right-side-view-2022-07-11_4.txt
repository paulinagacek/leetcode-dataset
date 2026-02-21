from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        
        # Queue has (node, level) elements
        bfs_queue = deque([(root, 1)])
        
        # result has the rightmost element in each level
        answer_dict = {}
        
        while bfs_queue:
            node, level = bfs_queue.popleft()
            answer_dict[level] = node.val
            if node.left:
                bfs_queue.append((node.left, level + 1))
            if node.right:
                bfs_queue.append((node.right, level + 1))
        
        return answer_dict.values()