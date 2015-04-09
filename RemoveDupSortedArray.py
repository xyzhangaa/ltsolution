###Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.
###Do not allocate extra space for another array, you must do this in place with constant memory.

###For example,
###Given input array A = [1,1,2],

###Your function should return length = 2, and A is now [1,2].

###swap
def RemoveDupSortedArray(A):
	if len(A) == 0:
		return []
	j =0
	for i in range(len(A)):
		if A[i] != A[j]:
			A[i],A[j+1] = A[j+1],A[i]
			j += 1
	del A[j+1:]
	return j+1
