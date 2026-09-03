"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) <= 1:
            return len(intervals)

       
        res, curr = 0, 0
        starts, ends = [interval.start for interval in intervals], [interval.end for interval in intervals]
        ends.sort()
        starts.sort()
        
        s, e = 0, 0
        while s < len(starts) and e < len(ends):
            if starts[s] < ends[e]:
                curr += 1
                s += 1
            else:
                curr -= 1
                e += 1
            res = max(res, curr)

        while s < len(starts):
            curr += 1
            s += 1



        return res