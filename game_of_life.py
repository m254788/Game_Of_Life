import numpy as np

n = 10
board = np.zeros((n,n))

def sum_neighbors(board,r,c):
	neighbors = []
	for i in range(r-1,r+2):
		for j in range(c-1,c+2):
			if [i,j] != [r,c]:
				neighbors.append(board[i,j])
	return sum(neighbors)

def tick(board_in, n):
	board_out = np.zeros(board_in.shape)
	for i in range(1,n-1):
		for j in range(1,n-2):
			if board_in[i][j]:
				if sum_neighbors(board_in, i, j) in [2,3]:
					board_out[i][j] = 1
				else:
					board_out[i][j] = 0
			else:
				if sum_neighbors(board_in, i, j) == 3:
					board_out[i][j] = 1
				else:
					board_out[i][j] = 0
	return board_out




				
			


