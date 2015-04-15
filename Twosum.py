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
  
