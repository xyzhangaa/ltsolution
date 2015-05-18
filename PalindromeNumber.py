####Determine whether an integer is a palindrome. Do this without extra space.
def getdigit(num):
	result = 1
	while num/10 != 0:
		result+=1
		num /= 10
	return result
def isdigitPalindrome(num):
	if num < 0:
		return False
	else:
		digit = getdigit(num)
		if digit == 1:
			return True
		else:
			low = 1
			while digit > low:
				if num%(10**digit)//(10**(digit-1)) \
				   == num%(10**low)//(10**(low-1)):
					digit -= 1
					low += 1
				else:
					return False
					break
			else:
				return True

# Time:  O(1)
# Space: O(1)
#
# Determine whether an integer is a palindrome. Do this without extra space.
# 
# Some hints:
# Could negative integers be palindromes? (ie, -1)
# 
# If you are thinking of converting the integer to string, note the restriction of using extra space.
# 
# You could also try reversing an integer. However, if you have solved the problem "Reverse Integer", 
# you know that the reversed integer might overflow. How would you handle such case?
# 
# There is a more generic way of solving this problem.
#

class Solution:
    # @return a boolean
    def isPalindrome(self, x):
        if x < 0:
            return False
        copy, reverse = x, 0
        
        while copy:
            reverse *= 10
            reverse += copy % 10
            copy /= 10
        
        return x == reverse

if __name__ == "__main__":
    print Solution().isPalindrome(12321)
    print Solution().isPalindrome(12320)
    print Solution().isPalindrome(-12321)
