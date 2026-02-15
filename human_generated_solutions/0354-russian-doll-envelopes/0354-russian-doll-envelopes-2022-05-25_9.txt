class Solution:
    def binarySearch(self, heights, minHeight):
        start = 0
        end = len(heights)
        while start < end:
            mid = start + ((end - start) // 2)
            if heights[mid] < minHeight:
                start = mid + 1
            else:
                end = mid
        return start

    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key = lambda x: (x[0], -x[1]))
        
        heights = [h for _, h in envelopes]
        lis = []
        
        for height in heights:
            idx = self.binarySearch(lis, height)
            if idx == len(lis):
                lis.append(height)
            else:
                lis[idx] = height

        return len(lis)