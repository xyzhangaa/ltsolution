# Time:  O(1)
# Space: O(1)
#
# Given a range [m, n] where 0 <= m <= n <= 2147483647, 
# return the bitwise AND of all numbers in this range, inclusive.
#
# For example, given the range [5, 7], you should return 4.
#

class Solution:
  def bitwisenumrange(self,m,n):
    i,diff= 0,n-m
    while diff:
      diff >>= 1
      i += 1
    return n&m >> i << i
    
class Solution2:
    def bitwisenumrange(self,m,n):
       p =0
       while m != n:
         m >>= 1
         n >>= 1
         p += 1
      return m << p
