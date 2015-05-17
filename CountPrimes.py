###Count the number of prime numbers less than a non-negative number, n

###http://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

class Solution:
  def countprimes(self,n):
    isPrime = [True]*max(n,2)
    isPrime[0],isPrime[1] = False,False
    x = 2
    while x*x< n:
      if isPrime[x]:
        p = x*x
        while p<n:
          isPrime[p] = False
          p += x
      x += 1
    return sum(isPrime)
