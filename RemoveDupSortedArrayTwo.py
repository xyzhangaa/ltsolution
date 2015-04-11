###Follow up for "Remove Duplicates":
###What if duplicates are allowed at most twice?

###For example,
###Given sorted array A = [1,1,1,2,2,3],

###Your function should return length = 5, and A is now [1,1,2,2,3].


def RemoveDupSortedArrayTwo(A):
	if len(A) <= 2:
		return A
	prev = 1
	curr = 2
	while curr < len(A):
		if A[curr] == A[prev] and A[curr] == A[prev-1]:
			curr += 1
		else:
			prev += 1
			A[prev] = A[curr]
			curr += 1
	del A[prev+1:]
	return A, prev+1
