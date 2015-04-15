###Implement pow(x, n)

def pow(x,n):
  if  n == 0:
    return 1
  elif n < 0:
    return 1.0/(pow(x,-n))
  elif n ==1:
    return x
  else:
    if n%2 == 0:
      return pow(x*x,n//2)
    else:
      return pow(x*x,n//2)*x
      
