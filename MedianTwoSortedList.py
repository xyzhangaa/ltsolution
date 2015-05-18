###There are two sorted arrays A and B of size m and n respectively. 
###Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

# time O(log(m+n))
# time O(1)

def getKth(a,b,k):
	if len(a) > len(b):
		return getKth(b,a,k)
	if len(a) == 0:
		return b[k-1]
	if k == 1:
		return min(a[0],b[0])
	pa = min(floor(k/2),len(a))
	pb = int(k-pa)
	if a[pa-1] <= b[pb-1]:
		return getKth(a[pa:],b,pb)
	else:
		return getKth(a,b[pb:],pa)

def MedianTwoSortList(a,b):
	if (len(a)+len(b))%2 == 1:
		return getKth(a,b,(len(a)+len(b))/2)
	else:
		return (getKth(a,b,(len(a)+len(b))/2)+ \
		       getKth(a,b,(len(a)+len(b))/2+1))*0.5
