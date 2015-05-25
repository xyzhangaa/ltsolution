###Write a program to solve a Sudoku puzzle by filling the empty cells.

###Empty cells are indicated by the character '.'.

###You may assume that there will be only one unique solution.
#time O(9!*9)
#space O(1)

def SudokuSolver(board):
	def isValid(x,y):
		temp = board[x][y]
		board[x][y] = 'D'
		for i in range(9):
			if board[i][y] == temp:
				return False
		for i in range(9):
			if board[x][i] == temp:
				return False
		for i in range(3):
			for j in range(3):
				if board[(x/3)*3+i][(y/3)*3+j] == temp:
					return False
		board[x][y] = temp
		return True
		
	def dfs(board):
		for i in range(9):
			for j in range(9):
				if board[i][j] == '.':
					for k in '123456789':
						board[i][j] = k
						if isValid(i,j) and dfs(board):
							return True
						board[i][j] = '.'
					return False
		return True
	dfs(board)

if __name__ == "__main__":
    board = [['5', '3', '.', '.', '7', '.', '.', '.', '.'],
             ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
             ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
             ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
             ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
             ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
             ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
             ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
             ['.', '.', '.', '.', '8', '.', '.', '7', '9']]
    print Solution().solveSudoku(board)
