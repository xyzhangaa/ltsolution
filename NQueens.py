###The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.
###Given an integer n, return all distinct solutions to the n-queens puzzle.
###Each solution contains a distinct board configuration of the n-queens' placement, 
###where 'Q' and '.' both indicate a queen and an empty space respectively.


def NQueens(n):
	def check(k,j):
		for i in range(k):
			if board[i]==j or abs(k-i) == abs(board[i]-j):
				return False
		return True
	def dfs(depth, valuelist):
		if depth == n:
			res.append(valuelist)
			return
		for i in range(n):
			if check(depth,i):
				board[depth]=i
				s = '.'*n
				dfs(depth+1,valuelist+[s[:i]+'Q'+s[i+1:]])
	board = [-1 for _ in range(n)]
	res = []
	dfs(0,[])
	return res
