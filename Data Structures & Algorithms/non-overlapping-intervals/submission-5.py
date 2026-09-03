class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # [[1,2], [1,4], [2,4]] 
        # keep track of last non-overlapping, and always compare to that (bc deleted intervals should not count)
        intervals.sort()
        res = 0
        last_non_overlapping = None
        for i in range(1, len(intervals)):
            if last_non_overlapping is None:
                if intervals[i - 1][1] <= intervals[i][0]: # not overlap
                    last_non_overlapping = i
                else:
                    res += 1
                    if intervals[i - 1][1] < intervals[i][1]:
                        last_non_overlapping = i - 1
                    else: 
                        last_non_overlapping = i 

            else:
                if intervals[last_non_overlapping][1] <= intervals[i][0]: # not overlap
                    last_non_overlapping = i
                else:
                    res += 1
                    if intervals[last_non_overlapping][1] < intervals[i][1]:
                        continue
                    else: 
                        last_non_overlapping = i 


        return res