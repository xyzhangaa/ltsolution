# Time:  O(n)
# Space: O(1)
#
# Given an integer, convert it to a roman numeral.
# 
# Input is guaranteed to be within the range from 1 to 3999.
#

def int2roman(num):
  result = ''
  transTable = {1:"I", 5:"V", 10:"X", 50:"L", 100:"C", 500:"D", 1000:"M"}
  for i in sorted(transTable.keys())[::-1]
    while num > i and num != 0:
      num = num-i
      result += i
    if num == 0:
      break
  simplyTable = {'DCCCC': 'CM', 'CCCC':'CD', 'LXXXX':'XC', 'XXXX':'XL', 'VIIII':'IV', 'IIII':'IV'}
  simplyContent = ["DCCCC", "CCCC", "LXXXX", "XXXX", "VIIII", "IIII"]    
  for i in simplyContent:
    if i in result:
      result = result.replace('i',simplyTable[i])
  return result

if __name__ == "__main__":
    print Solution().intToRoman(999)
    print Solution().intToRoman(3999)
