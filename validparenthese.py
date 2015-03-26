###Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
###The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

def validparenthese(s):
  matchparenthese = {'(' : ')', '[':']', '{':'}'}
  stack = []
  for element in s:
    if element == '(' or element =='[' or element == '{':
      stack.append(element)
    elif element == '(' or element ==']' or element == '}':
      if stack.pop() != element or len(stack) == 0:
        return False
        break
      else:
        pass
  return len(stack) == 0
