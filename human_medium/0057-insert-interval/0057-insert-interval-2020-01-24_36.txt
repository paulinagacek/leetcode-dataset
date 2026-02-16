class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []
        x0, y0 = newInterval
        i = 0
        while i < len(intervals) and y0 >= intervals[i][0]:
            x, y = intervals[i]
            if y < x0: ans.append(intervals[i])
            else: x0, y0 = min(x0, x), max(y0, y)
            i += 1
        ans.append([x0, y0])
        ans.extend(intervals[i:])
        return ans
