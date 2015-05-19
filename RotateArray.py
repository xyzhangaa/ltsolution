# Time:  O(n)
# Space: O(1)
#
# Rotate an array of n elements to the right by k steps.
#
# For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].
#
# Note:
# Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
#

class Solution:
  def rotatearr(self,nums,k):
    k %= len(nums)
    self.reverse(nums,0,len(nums))
    self.reverse(nums,0,k)
    self.reverse(nums,k,len(nums))
  
  def reverse(self,nums,start,end):
    while start < end:
    nums[start], nums[end-1] = nums[end-1],nums[start]
    start += 1
    end -=1
  
from fractions import gcd
class Solution2:
  def rotatearr(self,nums,k):
    k %= len(nums)
    num_cycle = gcd(len(nums),k)
    cycle_len = len(nums)/num_cycle
    for i in range(num_cycle):
    self.apply_cycle_permutation(k,i,cycle_len,nums)
  
  def apply_cycle_permutation(self,k,offset,cycle_len,nums):
    temp = nums[offset]
    for i in range(1,cycle_len):
      nums[(offset+i*k) % len(nums)], temp = temp,nums[(offset+i*k) % len(nums)]
    nums[offset] = temp
