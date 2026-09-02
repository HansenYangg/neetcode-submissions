class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        if not intervals:
            return [newInterval]

        res, inserted = [], False
        for i in range(len(intervals)):
            # case 1 - newInterval is inserted after intervals[i], can append intervals[i] normally
            if newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            # case 2 - newInterval is inserted before intervals[i]
            elif newInterval[1] < intervals[i][0]:
                inserted = True
                res.append(newInterval)
                return res + intervals[i:]
                

            # case 3 - newInterval is inserted in between prev interval and intervals[i]
            else:
                newInterval = [min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1])]




        if not inserted:
            res.append(newInterval)
# res = [[1, 3]]
#[[1, 3], [10, 15]] --- [4, 6]

        return res

        