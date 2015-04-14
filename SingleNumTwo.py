###Given an array of integers, every element appears three times except for one. Find that single one.

def SingleNumTwo(A):
	one = 0
	two = 0
	three = 0
	for i in range(len(A)):
		two |= A[i] & one
		one = A[i] ^ one
		three = ~(one & two)
		one &= three
		two &= three
	return one
