class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        if not intervals:
            return [newInterval]

        res = []
        inserted = False

        for idx, interval in enumerate(intervals):
            if interval[1] < newInterval[0]:
                res.append(interval)

            elif newInterval[1] < interval[0]:
                res.append(newInterval)
                return res + intervals[idx:]

            
            else:
                newInterval = [min(interval[0], newInterval[0]), max(interval[1], newInterval[1])]


        if not inserted:
            res.append(newInterval)

        return res