###Given a triangle, find the minimum path sum from top to bottom. 
###Each step you may move to adjacent numbers on the row below.

def Triangle(array):
	if len(array) == 0:
		return 0
	arr = [0 for _ in range(len(array))]
	arr[0] = array[0][0]
	for i in range(1,len(array)):
		for j in range(len(array[i])-1,-1,-1):
			if j == len(array[i])-1:
				arr[j] = arr[j-1]+array[i][j]
			elif j == 0:
				arr[j] = arr[j]+array[i][j]
			else:
				arr[j] = min(arr[j-1],arr[j])+array[i][j]
	return min(arr)
