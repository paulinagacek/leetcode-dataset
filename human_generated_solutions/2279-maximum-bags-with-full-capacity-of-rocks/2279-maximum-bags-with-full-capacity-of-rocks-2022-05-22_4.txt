class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        left = [0]*len(capacity)
        for i in range(len(capacity)):
            left[i] = capacity[i]-rocks[i]
        left.sort()
        ans = 0 
        while ans < len(left) and additionalRocks > 0:
            if additionalRocks >= left[ans]:
                additionalRocks -= left[ans]
                ans += 1
            else:
                break
        return ans