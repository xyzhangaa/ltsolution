###Given two binary strings, return their sum (also a binary string).
###For example,
###a = "11"
###b = "1"
###Return "100".

def AddBinary(a,b):
	aIndex = len(a)-1
	bIndex = len(b)-1
	carry = 0
	s = ''
	while aIndex >= 0 and bIndex>= 0:
		num = int(a[aIndex])+int(b[bIndex])+carry
		carry = num//2
		num = num%2
		s = str(num) + s
		aIndex -=1
		bIndex -= 1
	while aIndex >= 0:
		num = int(a[aIndex])+carry
		carry = num//2
		num = num%2
		s = str(num) + s
		aIndex -= 1
	while bIndex >= 0:
		num = int(b[bIndex])+carry
		carry = num//2
		num = num%2
		s = str(num) + s
		bIndex -= 1
	if carry == 1:
		s = '1'+s
	return s
