def removeDup(A):
	if len(A) <= 1:
		return 0,A
	else:
		current, origin = 1,1
		while origin < len(A):
			if A[origin] != A[origin-1]:
				A[current] = A[origin]
				current += 1
			origin += 1
		return current, A[0:current]
