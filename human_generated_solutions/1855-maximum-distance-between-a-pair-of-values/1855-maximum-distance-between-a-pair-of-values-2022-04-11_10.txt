class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        i, j, max_dist = 0, 0, 0
        for j in range(len(nums2)):
            if nums1[i] > nums2[j]:
                i += 1
                if i == len(nums1):
                    break
            else:
                max_dist = max(max_dist, j - i)
        return max_dist