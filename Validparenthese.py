# Time:  O(n)
# Space: O(n)
#
# Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid.
# 
# The brackets must close in the correct order, "()" and "()[]{}" 
# are all valid but "(]" and "([)]" are not.
#

def validparenthese(s):
  matchparenthese = {'(' : ')', '[':']', '{':'}'}
  stack = []
  for element in s:
    if element == '(' or element =='[' or element == '{':
      stack.append(element)
    elif element == ')' or element ==']' or element == '}':
      if len(stack) == 0:
        return False
        break
      elif stack.pop() != matchparenthese[element]:
        return False
        break
      else:
        continue
  return len(stack) == 0
