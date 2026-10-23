class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # [[1,2], [1,4], [2,4]] 
        # keep track of last non-overlapping, and always compare to that (bc deleted intervals should not count)
        intervals.sort()
        res, lastEnd = 0, intervals[0][1]
     
        for i in range(1, len(intervals)):
            if intervals[i][0] >= lastEnd:
                lastEnd = intervals[i][1]
            else:
                res += 1
                lastEnd = min(lastEnd, intervals[i][1])

        return res