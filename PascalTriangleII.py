def PascalTriangle(nRows):
	if nRows == 0:
		return []
	if nRows == 1:
		return [[1]]
	if nRows == 2:
		return [[1],[1,1]]
	if nRows > 2:
		list = [[] for _ in range(nRows+1)]
		for i in range(0,nRows):
			list[i] = [1 for j in range(i+1)]
		for i in range(2,nRows+1):
			for j in range(1,i):
				list[i][j]=list[i-1][j-1]+list[i-1][j]
		return list[nRows]
