###Given an array of integers, every element appears twice except for one. Find that single one.
#O(n), O(1)
def SingleNum(A):
	res = A[0]
	for i in range(1,len(A)):
		res = res ^ A[i]
	return res
