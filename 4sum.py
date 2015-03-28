###Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? 
###Find all unique quadruplets in the array which gives the sum of target.

def 4sum(S,target):
      result = []
      num.sort()
      firstIndex = 0
      while firstIndex < len(num)-3:
          secondIndex = firstIndex + 1
          while secondIndex < len(num)-2:                
              thirdIndex = secondIndex + 1
              fourthIndex = len(num) - 1
 
              while thirdIndex < fourthIndex:
                  if num[firstIndex] + num[secondIndex] + num[thirdIndex] \
                     + num[thirdIndex] > target:
                      break
                  if num[firstIndex] + num[secondIndex] + num[fourthIndex] \
                     + num[fourthIndex] < target:
                      break
 
                  temp = num[firstIndex] + num[secondIndex] + num[thirdIndex] \
                       + num[fourthIndex]
                  if temp == target:
                      result.append([num[firstIndex], num[secondIndex], \
                                     num[thirdIndex], num[fourthIndex]])
                      thirdIndex += 1
                      while thirdIndex < fourthIndex + 1 and \
                            num[thirdIndex] == num[thirdIndex-1]:
                          thirdIndex += 1
                      fourthIndex -= 1
                      while fourthIndex > thirdIndex -1 and \
                            num[fourthIndex] == num[fourthIndex+1]:
                          fourthIndex -= 1
                  elif temp > target:
                      fourthIndex -= 1
                      while fourthIndex > thirdIndex -1 and \                              
                                num[fourthIndex] == num[fourthIndex+1]:
                            fourthIndex -= 1
                  else:
                      thirdIndex += 1
                      while thirdIndex < fourthIndex + 1 and \
                            num[thirdIndex] == num[thirdIndex-1]:
                          thirdIndex += 1
 
          secondIndex += 1
              while secondIndex < len(num)-1 and \
                    num[secondIndex] == num[secondIndex-1]:
                  secondIndex += 1
 
          firstIndex += 1
          while firstIndex < len(num) - 2 and \
                num[firstIndex] == num[firstIndex-1]:
              firstIndex += 1
      return result
