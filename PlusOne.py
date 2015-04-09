###Given a non-negative number represented as an array of digits, plus one to the number.
###The digits are stored such that the most significant digit is at the head of the list.

def PlusOne(num):
	carry = 1
	for i in range(len(num)-1,-1,-1):
		if (num[i]+carry) >= 10:
			num[i] = (num[i]+carry)%10
			carry = 1
		else:
			num[i] = num[i]+carry
			carry = 0
	if carry == 1:
		num.insert(0,1)
	return num
