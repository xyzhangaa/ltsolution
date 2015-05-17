###A peak element is an element that is greater than its neighbors.

###Given an input array where num[i] ≠ num[i+1], find a peak element and return its index.

###The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

###You may imagine that num[-1] = num[n] = -∞.

###For example, in array [1, 2, 3, 1], 3 is a peak element and your function should return the index number 2.

###O(n): brute force
class Solution:
  def peakelement(self,nums):
    size = len(nums)
    for i in range(1,size-1):
      if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
        return i
    return [0,size-1][nums[0] < nums[size-1]]
    
###O(logn): binary search
class Solution:
  def peakelement(self,nums):
    size = len(nums)
    return self.search(nums,0,size-1)
  def search(self,nums,start,end):
    if start == end:
      return start
    if start+1 = end:
      return [start,end][nums[start] < nums[end]]
    mid = (start+end)/2
    if nums[mid] < nums[mid-1]:
      return self.searth(nums,start,mid-1)
    if nums[mid] < nums[mid+1]:
      return self.search(nums,mid+1,end)
    return mid
