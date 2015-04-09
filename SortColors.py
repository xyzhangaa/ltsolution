###Given an array with n objects colored red, white or blue, sort them so that 
###objects of the same color are adjacent, with the colors in the order red, white and blue.

###Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

###Note:
###You are not suppose to use the library's sort function for this problem.

def SortColors(A):
	if A == []:
		return []
	p1 = 0
	p2 = len(A)-1
	i =0
	while i <= p2:
		if A[i] == 2:
			A[i],A[p2] = A[p2],A[i]
			p2 -= 1
		elif A[i] == 0:
			A[i],A[p1] = A[p1],A[i]
			p1 += 1
			i += 1
		else:
			i += 1
	return A
