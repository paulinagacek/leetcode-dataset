class Solution:
    def merge(self, intervals):
        intervals.sort()
        output = []
        start = intervals[0][0]
        end = intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][0] > end:  # non-overlapping
                output.append([start, end])
                start = intervals[i][0]
                end = intervals[i][1]
            else:  # overlapping
                if intervals[i][1] > end:
                    end = intervals[i][1]
        output.append([start, end])
        return output
