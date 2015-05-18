###Given a sorted array and a target value, return the index if the target is found. 
###If not, return the index where it would be if it were inserted in order.
###You may assume no duplicates in the array.
#time O(logn)
#space O(1)

def searchinsertpos(A,target):
  begin,end = 0, len(A)-1
  insertpos = 0
  while begin <= end:
    mid = (begin+end)//2
    if A[mid] == target:
      return mid
    elif A[mid] > target:
      end = mid-1
      insertpos = mid
    else:
      begin = mid+1
      insertpos=mid+1
  return insertpos

if __name__ == "__main__":
    print Solution().searchInsert([1, 3, 5, 6], 5)
    print Solution().searchInsert([1, 3, 5, 6], 2)
    print Solution().searchInsert([1, 3, 5, 6], 7)
    print Solution().searchInsert([1, 3, 5, 6], 0)
