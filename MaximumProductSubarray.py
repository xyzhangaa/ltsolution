###Find the contiguous subarray within an array (containing at least one number) which has the largest product

def maxproductnonzero(A):
	i = 0
	negnum = 0
	negindex = []
	while i < len(A):
		if A[i]<0:
			negnum += 1
			negindex.append(i)
		i += 1
	if negnum%2 == 0:
		result = reduce(lambda x,y: x*y, A,1)
	else:
		firstlag = reduce(lambda x,y: x*y, A[0:negindex[-1]],1)
		lastlag = reduce(lambda x,y: x*y, A[negindex[0]+1:],1)
		result = max(firstlag,lastlag)
	return result

def maxproduct(B):
	i = 0
	subB = []
	maxproduct = 0
	while i < len(B):
		if B[i] != 0:
			subB.append(B[i])
		else:
			maxproduct = max(maxproduct,maxproductnonzero(subB))
			subB = []
		i += 1
	else:
		maxproduct = max(maxproduct,maxproductnonzero(subB))
	return maxproduc
