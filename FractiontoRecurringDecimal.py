###Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

###If the fractional part is repeating, enclose the repeating part in parentheses.

###For example,

###Given numerator = 1, denominator = 2, return "0.5".
###Given numerator = 2, denominator = 1, return "2".
###Given numerator = 2, denominator = 3, return "0.(6)".

class Solution:
  def fractiontorecurringdecimal(self,numerator,denominator):
    negativeflag = numerator*denominator <0
    numerator = abs(numerator)
    denominator = abs(denominator)
    numlist = []
    count = 0
    loopdict = dict()
    loopstr = None
    while True:
      numlist.append(str(numerator/denominator))
      count += 1
      numerator = 10*(numerator%denominator)
      if numerator == 0:
        break
      loc = loopdict.get(numerator)
      if loc:
        loopstr = ''.join(numlist[loc:count])
        break
      loopdict[numerator] = count
    ans = numlist[0]
    if len(numlist) > 1:
      ans += '.'
    if loopstr:
      ans += ''.join(numlist[1:len(numlist)-len(loopstr)])+'('+loopstr+')'
    else:
      ans += '.'join(numlist[1:])
      if negativeflag:
        ans = '-'+ans
    return ans
