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
  if s[i] in '-+':
    i += 1
  while i < len(s) and s[i].isdigit():
    result = result*10+(ord(str[i])-ord('0'))*sign
    i += 1
    if sign == 1 and result >= int_max:
      return int_max
    elif sign == -1 and result <= int_min:
      return int_min
  return result
