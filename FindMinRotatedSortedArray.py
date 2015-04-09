###Suppose a sorted array is rotated at some pivot unknown to you beforehand.
###(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

###Find the minimum element.

###You may assume no duplicate exists in the array.

def FindMinRotatedSortedArray(A):
	left = 0
	right = len(A)-1
	while left < right and A[left] > A[right]:
		center = (left+right)//2
		if A[center] < A[right]:
			right = center
		else:
			left = center+1
	return A[left]
