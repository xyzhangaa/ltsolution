###The count-and-say sequence is the sequence of integers beginning as follows:
###1, 11, 21, 1211, 111221, ...
###1 is read off as "one 1" or 11.
###11 is read off as "two 1s" or 21.
###21 is read off as "one 2, then one 1" or 1211.
###Given an integer n, generate the nth sequence.

def counts(self,s):
  count = 0
  current = '#'
  result = ''
  for item in s:
    if item != current:
      if current!='#':
        result += str(count)+current
      count = 1
      current = item
    else:
      count += 1
  result += str(count)+current
  return result

def countandsay(self,n):
  string = '1'
  for i in range(2,n+1):
    string = self.counts(string)
  return string
