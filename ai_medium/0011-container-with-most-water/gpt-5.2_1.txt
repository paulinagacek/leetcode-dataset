class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        best = 0
        while l < r:
            if height[l] < height[r]:
                best = max(best, (r - l) * height[l])
                l += 1
            else:
                best = max(best, (r - l) * height[r])
                r -= 1
        return best
