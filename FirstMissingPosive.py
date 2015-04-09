###Given an unsorted integer array, find the first missing positive integer.

###For example,
###Given [1,2,0] return 3,
###and [3,4,-1,1] return 2.

###Your algorithm should run in O(n) time and uses constant space.

###swap

def firstmissingpos(A):
	i = 0
	while i <= len(A)-1:
		if i+1 == A[i]:
			i+= 1
		elif A[i] <= 0:
			i+=1
		elif A[i] > len(A):
			i+=1
		elif A[i] == A[A[i]-1]:
			i+=1
		else:
			tmpa,tmpb = i, A[i]-1
			A[tmpa],A[tmpb] = A[tmpb],A[tmpa]
	for i in range(len(A)):
		if i+1 != A[i]:
			return i+1
	return len(A)+1
