import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
        heap = []
        for i in nums:
            heapq.heappush(heap, i)
            if len(heap) > k:
                heapq.heappop(heap)
        return heapq.heappop(heap)
        
        # this is a min heap and since we are removing smallest node from the heap root each time the lenght exceeds k, at the end of the loop we\'ll be having the largest element at the root of the heap, just pop and return