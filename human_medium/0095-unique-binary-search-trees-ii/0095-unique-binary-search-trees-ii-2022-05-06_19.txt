class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        return self.rec(list(range(1, n+1)))
    
    def rec(self, nums):
        return [TreeNode(val=nums[i], left=left, right=right)
                for i in range(len(nums))
                for left in self.rec(nums[:i])
                for right in self.rec(nums[i+1:])] or [None]
