###Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

###If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

###The replacement must be in-place, do not allocate extra memory.

###Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
###1,2,3 → 1,3,2
###3,2,1 → 1,2,3
###1,1,5 → 1,5,1

def nextpermutation(A):
	if len(A)<=1:
		return A
	partition = -1
	for i in range(len(A)-2,-1,-1):
		if A[i] < A[i+1]:
			partition = i
			break
	if partition == -1:
		return A.reverse()
	else:
		for i in range(len(A)-1,partition,-1):
			if A[i] > A[partition]:
				A[i],A[partition] = A[partition],A[i]
				break
	left = partition+1
	right = len(A)-1
	while left< right:
		A[left],A[right] = A[right],A[left]
		left += 1
		right -= 1
	return A
