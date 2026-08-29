"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        print(intervals)
        if len(intervals)<=1:
            return True
        intervals.sort(key=lambda x:x.start)
        print([[interval.start,interval.end] for interval in intervals])
        prev_end=intervals[0].end
        for interval in intervals[1:]:
            if interval.start<prev_end:
                return False
            prev_end=interval.end
        return True