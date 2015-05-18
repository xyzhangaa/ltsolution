###Suppose a sorted array is rotated at some pivot unknown to you beforehand.
###(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
###You are given a target value to search. If found in the array return its index, otherwise return -1.
###You may assume no duplicate exists in the array.
#time (logn)
#space O(1)

def _searchtargethelper(A,target,begin,end):
	if begin > end:
		return -1
	mid = (begin+end)//2
	if A[begin] < A[end]:
		rotate = False
	else:
		rotate = True
	if A[mid] == target:
		return mid
	elif A[mid] > target:
		if rotate:
			temp = _searchtargethelper(A,target,mid+1,end)
			if temp != -1:
				return temp
		return _searchtargethelper(A,target,begin,mid-1)
	else:
		if rotate:
			temp = _searchtargethelper(A,target,begin,mid-1)
			if temp != -1:
				return temp
		return _searchtargethelper(A,target,mid+1,end)

def searchtarget(A,target):
	return _searchtargethelper(A,target,0,len(A)-1)


#####
class Solution2:
	def search(self, A, target):
        	low, high = 0, len(A)
        
        	while low < high:
            	mid = low + (high - low) / 2
            
            	if A[mid] == target:
                	return mid
            
            	if A[low] <= A[mid]:
                	if A[low] <= target and target < A[mid]:
                    		high = mid
                	else:
                    	low = mid + 1
            	else:
                	if A[mid] < target and target <= A[high - 1]:
                    		low = mid + 1
                	else:
                    		high = mid
                    
        	return -1
