'''
352. Data Stream as Disjoint Intervals

Given a data stream input of non-negative integers a1, a2, ..., an, ..., summarize the numbers seen so far as a
list of disjoint intervals.

For example, suppose the integers from the data stream are 1, 3, 7, 2, 6, ..., then the summary will be:

[1, 1]
[1, 1], [3, 3]
[1, 1], [3, 3], [7, 7]
[1, 3], [7, 7]
[1, 3], [6, 7]
Follow up:
What if there are lots of merges and the number of disjoint intervals are small compared to the data stream's size?


Reference:
    57. Insert Interval
'''


# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class SummaryRanges(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.intervals = []

    def addNum(self, val):
        """
        :type val: int
        :rtype: void
        """
        results = []
        insertPos = 0
        new_interval = Interval(val, val)
        for interval in self.intervals:
            if interval.end < new_interval.start - 1:
                results.append(interval)
                insertPos += 1
            elif interval.start > new_interval.end + 1:
                results.append(interval)
            else:  # interval.end >= newInterval.start and interval.start <= newInterval.end
                new_interval.start = min(interval.start, new_interval.start)
                new_interval.end = max(interval.end, new_interval.end)
        results.insert(insertPos, new_interval)
        self.intervals = results

    def getIntervals(self):
        """
        :rtype: List[Interval]
        """
        return self.intervals


# Your SummaryRanges object will be instantiated and called as such:
obj = SummaryRanges()
obj.addNum(1)
obj.addNum(3)
obj.addNum(2)

param_2 = obj.getIntervals()
print param_2
