###Given a collection of intervals, merge all overlapping intervals.
###For example,
###Given [1,3],[2,6],[8,10],[15,18],
###return [1,6],[8,10],[15,18].

def MergeIntervals(intervals):
  intervals.sort(key = lambda x:x[0])
  result  = intervals[0]
  for i in range(1,len(intervals)):
    size = len(result):
    if result[size-1][0] <= intervals[i][0] <= result[size-1][1]:
      result[size-1][1] = max(result[size-1][1],intervals[i][1])
    else:
      result.append(intervals[i])
  return result
