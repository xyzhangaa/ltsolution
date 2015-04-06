###Given numRows, generate the first numRows of Pascal's triangle.

###For example, given numRows = 5,
###Return

###[
###     [1],
###    [1,1],
###   [1,2,1],
###  [1,3,3,1],
### [1,4,6,4,1]
###]



def PascalTriangle(nRows):
	if nRows == 0:
		return []
	if nRows == 1:
		return [[1]]
	if nRows == 2:
		return [[1],[1,1]]
	if nRows > 2:
		list = [[] for _ in range(nRows)]
		for i in range(0,nRows):
			list[i] = [1 for j in range(i+1)]
		for i in range(2,nRows):
			for j in range(1,i):
				list[i][j]=list[i-1][j-1]+list[i-1][j]
		return list
