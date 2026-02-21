class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        arr1,arr2=[],[]
        self.helper1(root1,arr1)
        self.helper1(root2,arr2)
        ans=arr1+arr2
        ans.sort()
        return (ans)
        
    def helper1(self,root1,arr1):
        if root1:
            self.helper1(root1.left, arr1)
            arr1.append(root1.val)
            self.helper1(root1.right,arr1)