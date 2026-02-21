class Solution:

    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        return self.__generate(lo=1, hi=n)

    @classmethod
    @cache
    def __generate(cls, lo: int, hi: int) -> list:
        if lo > hi:
            return [None]
        return [
            TreeNode(root, left, right)
            for root in range(lo, hi + 1)              # All possible roots for the current subarray
            for left in cls.__generate(lo, root - 1)   # All possible trees to the left of the root element
            for right in cls.__generate(root + 1, hi)  # All possible trees to the right of the root element
        ]