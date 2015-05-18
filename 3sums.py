# Time:  O(n^2)
# Space: O(1)
#
# Given an array S of n integers,
# are there elements a, b, c in S such that a + b + c = 0?
# Find all unique triplets in the array which gives the sum of zero.
#
# Note:
# Elements in a triplet (a,b,c) must be in non-descending order. (ie, a <= b <= c)
# The solution set must not contain duplicate triplets.
#    For example, given array S = {-1 0 1 2 -1 -4},
#
#    A solution set is:
#    (-1, 0, 1)
#    (-1, -1, 2)
#

def 3sum(nums):
  nums.sort()
  i = 0
  result = []
  while i < len(nums)-2:
    j = i+1
    k = len(nums)-1
    while j < k:
      if nums[i]+nums[j]+nums[j+1] > 0 or nums[i]+nums[k-1]+nums[k] < 0:
        break
      if nums[i]+nums[j]+nums[k] == 0:
        result.append([nums[i],nums[j],nums[k]])
        j += 1
        while nums[j] == nums[j+1] and j < k+1:
          j +=1
        while nums[k] == nums[k+1] and k > j-1:
          k -= 1
        k -= 1
      elif nums[i]+nums[j]+nums[k] > 0:
        k -= 1
        while nums[k] == nums[k-1] and k > j-1:
          k -= 1
      else:
        j += 1
        while nums[j] == nums[j+1] and k > j-1:
          j +=1
    i += 1
    while nums[i] == nums[i+1] and i < len(nums)-1:
      i += 1
  return result

if __name__ == '__main__':
    result = Solution().threeSum([-1, 0, 1, 2, -1, -4])
    print result
    
    
