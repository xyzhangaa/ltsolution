### implement atoi

def atoi(s):
  int_max, int_min = 2147483647, -2147483648
  result = 0
  sign = 1
  i = 0
  if len(s) == 0:
    return 0
  while s[i].isspace():
    i += 1
  if s[i] == '-':
    sign = -1
    i+=1
    if not (str[i] >= '0' and str[i] <= '9'):
      return 0
  if s[i] == '+':
    i += 1
    if not (str[i] >= '0' and str[i] <= '9'):
      return 0
  while i < len(s) and s[i].isdigit():
    result = result*10+(ord(str[i])-ord('0'))*sign
    i += 1
    if sign == 1 and result >= int_max:
      return int_max
    elif sign == -1 and result <= int_min:
      return int_min
  return result

# Time:  O(n)
# Space: O(1)
#
# Implement atoi to convert a string to an integer.
# 
# Hint: Carefully consider all possible input cases. If you want a challenge, please do not see below 
# and ask yourself what are the possible input cases.
# 
# Notes: It is intended for this problem to be specified vaguely (ie, no given input specs).
# You are responsible to gather all the input requirements up front.
# 
# spoilers alert... click to show requirements for atoi.
# 
# Requirements for atoi:
# The function first discards as many whitespace characters as necessary 
# until the first non-whitespace character is found. Then, starting from this character, 
# takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.
# 
# The string can contain additional characters after those that 
# form the integral number, which are ignored and have no effect on the behavior of this function.
# 
# If the first sequence of non-whitespace characters in str is not a valid integral number, 
# or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.
# 
# If no valid conversion could be performed, a zero value is returned. 
# If the correct value is out of the range of representable values, INT_MAX (2147483647) or INT_MIN (-2147483648) is returned.
#

class Solution:
    # @return an integer
    def atoi(self, str):
        INT_MAX =  2147483647
        INT_MIN = -2147483648
        result = 0
        
        if not str:
            return result
        
        i = 0
        while i < len(str) and str[i] == " ":
            i += 1
        
        sign = 1
        if str[i] == "+":
            i += 1
            if not (str[i] >= '0' and str[i] <= '9'):
              return 0
        elif str[i] == "-":
            sign = -1
            i += 1
            if not (str[i] >= '0' and str[i] <= '9'):
                return 0
        while i < len(str) and str[i] >= '0' and str[i] <= '9':
            if result > INT_MAX / 10 or (result == INT_MAX / 10 and ord(str[i]) - ord('0') > INT_MAX % 10):
                if sign > 0:
                    return INT_MAX
                else:
                    return INT_MIN
            
            result = result * 10 + ord(str[i]) - ord('0')
            i += 1
        
        return sign * result

if __name__ == "__main__":
    print Solution().atoi("") 
    print Solution().atoi("-1")
    print Solution().atoi("2147483647") 
    print Solution().atoi("2147483648") 
    print Solution().atoi("-2147483648")  
    print Solution().atoi("-2147483649")  
