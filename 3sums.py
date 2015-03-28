###Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? 
###Find all unique triplets in the array which gives the sum of zero.

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

      
    
    
