class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        changed.sort()
        hq = []
        ans = []
        for i in range(len(changed)):
            if hq and hq[0] * 2 == changed[i]:
                ans.append(heapq.heappop(hq))
            else:
                heapq.heappush(hq, changed[i]) 
        return ans if not hq else []