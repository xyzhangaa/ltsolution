###The count-and-say sequence is the sequence of integers beginning as follows:
###1, 11, 21, 1211, 111221, ...
###1 is read off as "one 1" or 11.
###11 is read off as "two 1s" or 21.
###21 is read off as "one 2, then one 1" or 1211.
###Given an integer n, generate the nth sequence.

def count(s):
  count = 0
  current = '#'
  result = ''
  for item in s:
    if item != current:
      if current!='#':
        result += str(count)+current
    else:
      count += 1
  return result

def countandsay(s,n):
  string = str(s)
  for i in range(2,n+1):
    string = count(string)
  return string
