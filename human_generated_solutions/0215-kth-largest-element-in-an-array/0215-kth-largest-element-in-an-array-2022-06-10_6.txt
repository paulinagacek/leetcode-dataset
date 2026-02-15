import heapq
class Solution:
    def findKthLargest(self, nums, k):
        self.minHeap = []     # as root of min heap is minimum and root is removed in pop operation
        self.heapLength = 0   # for calculating length of heap in constant time else len() would take O(k) time
        
        def addToHeap(num):
            heapq.heappush(self.minHeap, num)
            self.heapLength += 1
            if self.heapLength > k:  # always trying to maintain heap length k 
                heapq.heappop(self.minHeap)
                self.heapLength -= 1
                
        for num in nums:        
            addToHeap(num)
        
        return self.minHeap[0]

# Time: O(N log(k))     ; O(N) for traversal and log(k) for pushing num to a heap of size k
# Space: O(k)           ; as the minHeap is always of size k