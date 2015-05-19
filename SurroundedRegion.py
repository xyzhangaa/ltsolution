###Given a 2D board containing 'X' and 'O', capture all regions surrounded by 'X'.

###A region is captured by flipping all 'O's into 'X's in that surrounded region.

###For example,

X X X X
X O O X
X X O X
X O X X
 

###After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X

#O(m*n), O(m*n)
def SurroundedRegions(board):
	if board == []:
		return []
	tokept = [[False for _ in range(len(board[0]))] for \
		  _ in range(len(board))]
	layer = []
	for column in range(len(board[0])):
		if board[0][column] == 'O':
			tokept[0][column] = True
			layer.append([0,column])
		if board[-1][column] == 'O':
			tokept[-1][column] = True
			layer.append([-1,column])
	for row in range(len(board)):
		if board[row][0] == 'O':
			tokept[row][0] = True
			layer.append([row,0])
		if board[row][-1] == 'O':
			tokept[row][-1] = True
			layer.append([row,-1])
	while len(layer) != 0:
		temp = []
		for keptnode in layer:
			if keptnode[0] != 0 and \
			   board[keptnode[0]-1,keptnode[1]] == 'O' and \
			   tokept[keptnode[0]-1,keptnode[1]] == False:
				tokept[keptnode[0]-1,keptnode[1]] = True
				temp.append([keptnode[0]-1,keptnode[1]])
			if keptnode[0] != -1 and \
			   board[keptnode[0]+1,keptnode[1]] == 'O' and \
			   tokept[keptnode[0]+1,keptnode[1]] == False:
				tokept[keptnode[0]+1,keptnode[1]] = True
				temp.append([keptnode[0]+1,keptnode[1]])
			if keptnode[1] != 0 and \
			   board[keptnode[0],keptnode[1]-1] == 'O' and \
			   tokept[keptnode[0],keptnode[1]-1] == False:
				tokept[keptnode[0],keptnode[1]-1] = True
				temp.append([keptnode[0],keptnode[1]-1])
			if keptnode[1] != -1 and \
			   board[keptnode[0],keptnode[1]+1] == 'O' and \
			   tokept[keptnode[0],keptnode[1]+1] == False:
				tokept[keptnode[0],keptnode[1]+1] = True
				temp.append([keptnode[0],keptnode[1]+1])
		layer = temp
	for row in range(len(board)):
		for column in range(len(board[0])):
			if board[row][column] == 'X':
				continue
			if tokept[row][column] == False:
				board[row][column] = 'X'
	return board

#O(m*n), O(m+n)
class Solution:
    # @param board, a 2D array
    # Capture all regions by modifying the input board in-place.
    # Do not return any value.
    def solve(self, board):
        if not board:
            return
        current = []
        
        for i in xrange(len(board)):
            current.append((i, 0))
            current.append((i, len(board[0]) - 1))
            
        for i in xrange(len(board[0])):
            current.append((0, i))
            current.append((len(board) - 1, i))
            
        while current:
            i, j = current.pop()
            if board[i][j] in ['O', 'V']:
                board[i][j] = 'V'
                for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                    if 0 <= x < len(board) and 0 <= y < len(board[0]) and board[x][y] == 'O':
                        board[x][y] = 'V'
                        current.append((x, y))
                        
        for i in xrange(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != 'V':
                    board[i][j] = 'X'
                else:
                    board[i][j] = 'O'

if __name__ == "__main__":
    board = [['X', 'X', 'X', 'X'],
             ['X', 'O', 'O', 'X'],
             ['X', 'X', 'O', 'X'],
             ['X', 'O', 'X', 'X']]
    Solution().solve(board)
    print board
