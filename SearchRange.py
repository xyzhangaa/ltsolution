###Given a sorted array of integers, find the starting and ending position of a given target value.

###Your algorithm's runtime complexity must be in the order of O(log n).

###If the target is not found in the array, return [-1, -1].

###For example,
###Given [5, 7, 7, 8, 8, 10] and target value 8,
###return [3, 4].

def searchrange(A,target):
	left = 0
	right = len(A)-1
	while left <= right:
		center = (left+right)//2
		if A[center] > target:
			right = center+1
		elif A[center] < target:
			left = center-1
		else:
			list = [0,0]
			if A[right] == target:
				list[1] = right
			if A[left] == target:
				list[0] = left
			for i in range(center,right+1):
				if A[i] != target:
					list[1] = i-1
					break
			for i in range(center,left-1,-1):
				if A[i] != target:
					list[0] = i+1
					break
			return list
	return [-1,-1]
