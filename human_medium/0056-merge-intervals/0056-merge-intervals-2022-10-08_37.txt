class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals)==1:
            return intervals
        intervals = sorted(intervals)
        
        res = []
        for i in range(1,len(intervals)):
     
            if res and intervals[i][0] <= res[-1][1]:
                if res[-1][1] >= intervals[i][1]:
                    continue
                else:
                    res.append([res.pop()[0],intervals[i][1]])
            
            elif intervals[i-1][1] >= intervals[i][0]:
                res.append([intervals[i-1][0],max(intervals[i][1],intervals[i-1][1])])
                
            else:
                res.append(intervals[i])
                
        if intervals[0][1] < intervals[1][0]: # if first to intervals never overlapped
            res = [intervals[0]]+res[:]
                
        return res
