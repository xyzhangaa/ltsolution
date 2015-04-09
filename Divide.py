
###Divide two integers without using multiplication, division and mod operator.

def divide(dividend,divisor):
	if (dividend < 0 and divisor > 0) or (dividend>0 and divisor <0):
		if abs(dividend) < abs(divisor):
			return 0
	total =0
	count = 0
	res = 0
	a = abs(dividend)
	b = abs(divisor)
	while a >= b:
		sum = b
		count = 1
		while sum+sum <= a:
			sum += sum
			count += count
		a -= sum
		res += count
	if (dividend < 0 and divisor > 0) or (dividend>0 and divisor <0):
		res = 0- res
	return res
