class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        stopCount = 0
		# We sort the `stations` by the amount of fuel descendingly.
        stations.sort(key = lambda x : x[1], reverse = True)
		# To check if our carrying fuel is enough to finish the course
        while startFuel < target:
            for i in range(len(stations)):
				# To check if the `stations[i]` is within our range.
                if stations[i][0] <= startFuel:
                    startFuel += stations[i][1]
                    stopCount += 1
                    stations.pop(i)
                    break
			# No available stations within our range OR no more stations left.
            else:
                return -1
        return stopCount