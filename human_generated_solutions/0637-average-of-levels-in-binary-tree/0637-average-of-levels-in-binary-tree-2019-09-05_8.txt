# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        #using dfs
        def preorder(node,depth,sum_count):
            if node == None:
                return 
            if depth>=len(sum_count):
                sum_count.append([0,0])
            sum_count[depth][0]+=node.val
            sum_count[depth][1]+=1
            preorder(node.left,depth+1,sum_count)
            preorder(node.right,depth+1,sum_count)
        if root == None:
            return []
        sum_count=[]
        ans=[]
        preorder(root,0,sum_count)
        for s in sum_count:
            ans.append(s[0]/s[1])
        return ans