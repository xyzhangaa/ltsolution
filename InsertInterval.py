###Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).
###You may assume that the intervals were initially sorted according to their start times.
###Example 1:
###Given intervals [1,3],[6,9], insert and merge [2,5] in as [1,5],[6,9].
###Example 2:
###Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] in as [1,2],[3,10],[12,16].
###This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].

#time O(nlogn)
#space O(1)
class Solution:
    def insert(self, intervals, newInterval):
        return self.merge(intervals + [newInterval])
        
    def merge(self, intervals):
        if not intervals:
            return intervals
        intervals.sort(key = lambda x: x.start)
        result = [intervals[0]]
        for i in xrange(1, len(intervals)):
            prev, current = result[-1], intervals[i]
            if current.start <= prev.end: 
                prev.end = max(prev.end, current.end)
            else:
                result.append(current)
        return result
	
if __name__ == "__main__":
    print Solution().merge([Interval(1, 3), Interval(2, 6), Interval(8, 10), Interval(15,18)])
