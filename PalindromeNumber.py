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
