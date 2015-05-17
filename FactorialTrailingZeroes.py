###Given an integer n, return the number of trailing zeroes in n!.

###Note: Your solution should be in logarithmic time complexity.

class Solution:
  def FactorialZeroes(self,n):
    x = 5
    ans = 0
    while n >= x:
      ans += n/x
      x *= 5
    return ans
