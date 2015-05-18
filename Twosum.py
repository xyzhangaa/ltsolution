##### output the indices (in ascending order) of two numbers in the array that sum up to equal to the target

def twosum(array,target):
  newarray = sorted.(enumerate(array), key=lambda x:x[1])
  begin,end=0,len(array)-1
  while begin != end:
    temp = newarray[begin][1]+newarray[end][1]
    if temp == target:
      if newarray[begin][0] < newarray[end][0]:
        return newarray[begin][0]+1, newarray[end][0]+1
      else:
        return newarray[end][0]+1, newarray[begin][0]+1
    elif temp < target:
      begin += 1
    else:
      end -= 1
  
#hash table solution
#time O(n)
#space O(n)
class Solution:
  def twosum(self,nums,target):
    lookup = {}
    for i,num in enumerate(nums):
      if target - num in lookup:
        return (lookup[target-num]+1,i+1)
      else:
        lookup[num] = i

if __name__ == '__main__':
  print 'index1=%d, index2=%d' %Solution.twosum((2,7,11,15),9)
