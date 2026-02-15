class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        l, h = 0, min(time) * totalTrips
        while l < h:
            mid = (l + h) // 2
            if sum([mid // i for i in time]) < totalTrips: l = mid + 1
            else: h = mid
        return l