###Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.
###The Sudoku board could be partially filled, where empty cells are filled with the character '.'.
###Note:
#A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.
#time O(n^2)
#space O(n)

def ValidSudoku(board):
	diction = {}
	for i in range(9):
		for j in range(9):
			if board[i][j] == '.':
				continue
			elif board[i][j] not in diction:
				diction[board[i][j]] = 1
			elif diction[board[i][j]] == 1:
				return False
		diction = {}
	for i in range(9):
		for j in range(9):
			if board[j][i] == '.':
				continue
			elif board[j][i] not in diction:
				diction[board[j][i]] = 1
			elif diction[board[j][i]] == 1:
				return False
		diction = {}
	for iblock in range(3):
		for jblock in range(3):
			for i in range(3):
				for j in range(3):
					if board[iblock*3+i][iblock*3+j] \
					   == '.':
						continue
					elif board[iblock*3+i][jblock*3+j] \
					     not in diction:
						diction[board[iblock*3+i] \
							[iblock*3+j]] = 1
					elif diction[board[iblock*3+i] \
						     [jblock*3+j]] == 1:
						return False
			diction = {}
	return True

if __name__ == "__main__":
    board = [[1, '.', '.', '.', '.', '.', '.', '.', '.'],
             ['.', 2, '.', '.', '.', '.', '.', '.', '.'],
             ['.', '.', 3, '.', '.', '.', '.', '.', '.'],
             ['.', '.', '.', 4, '.', '.', '.', '.', '.'],
             ['.', '.', '.', '.', 5, '.', '.', '.', '.'],
             ['.', '.', '.', '.', '.', 6, '.', '.', '.'],
             ['.', '.', '.', '.', '.', '.', 7, '.', '.'],
             ['.', '.', '.', '.', '.', '.', '.', 8, '.'],
             ['.', '.', '.', '.', '.', '.', '.', '.', 9]]
    print Solution().isValidSudoku(board)
