class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        pq = []
        stations.append((target, -1))
        refuel_stops = 0
        prev_location = 0
        for location, fuel in stations:
            startFuel -= location - prev_location
            while pq and startFuel < 0:
                startFuel += -heapq.heappop(pq)
                refuel_stops += 1
            if startFuel < 0:
                return -1
            heapq.heappush(pq, -fuel)
            prev_location = location
        return refuel_stops