###Given a string s consists of upper/lower-case alphabets and empty space characters ' ', 
###return the length of last word in the string.
###If the last word does not exist, return 0.

def lastword(s):
  return len(s.split()[len(s.split())-1] if s.split() != [] else 0


### if the special functions forbidden 

def lastword(s):
  i = len(s)-1
  count = 0
  while i >= 0:
    if s[i] == ' ':
      i -= 1
    else:
      break
  if i == len(s):
    return count
  else:
    while i >=0:
      if s[i] != ' ':
        count += 1
        i -= 1
      else:
        break
    return count
      
  
