###Write an algorithm to determine if a number is "happy".

###A happy number is a number defined by the following process: Starting with any positive integer, 
###replace the number by the sum of the squares of its digits, and repeat the process until the number 
###equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. 
###Those numbers for which this process ends in 1 are happy numbers.

class Solution:
  def isHappyNum(self,n):
    hset = set()
    while n != 1 and n not in hset:
      hset.add(n)
      while n :
        digit = n%10
        sum += digit**2
        n /= 10
      n = sum
    return n == 1
