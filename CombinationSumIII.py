#Find all possible combinations of k numbers that add up to a number n, given that only numbers 
#from 1 to 9 can be used and each combination should be a unique set of numbers.

#Ensure that numbers within the set are sorted in ascending order.

class Solution:
  def combinationsum3(self,k,n):
    ans = []
    def search(start,cnt,sums,nums):
      if cnt >k or sums > n:
        return 
      if cnt == k and sums ==n:
        ans.append(nums)
      for x in range(start+1,10):
        search(x,cnt+1,sums+x,nums+[x])
    search(0,0,0,[])
    return ans
