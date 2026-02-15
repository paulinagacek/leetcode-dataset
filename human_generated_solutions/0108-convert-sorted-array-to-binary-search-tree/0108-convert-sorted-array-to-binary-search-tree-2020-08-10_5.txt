def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def traverse(arr):
            if not arr: return
            m = (len(arr) - 1)//2
            node = TreeNode(arr[m])
            node.left = traverse(arr[:m])
            node.right = traverse(arr[m+1:])
            return node
        return traverse(nums)