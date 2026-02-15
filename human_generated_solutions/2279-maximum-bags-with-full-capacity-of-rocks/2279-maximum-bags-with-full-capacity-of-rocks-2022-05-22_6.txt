class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        l = []
        c = 0
        for i in range(len(capacity)):
            if capacity[i]-rocks[i]:
                l.append(capacity[i]-rocks[i])
            else:
                c+=1
        l.sort()
        for i in range(len(l)):
            a = l[i]
            if a<=additionalRocks:
                c+=1
                additionalRocks-=a 
            else:
                break
        return c