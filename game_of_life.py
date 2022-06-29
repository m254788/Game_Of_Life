import numpy as np
import random

def sum_neighbors(board,r,c):
	neighbors = []
	for i in range(r-1,r+2):
		for j in range(c-1,c+2):
			if [i,j] != [r,c]:
				neighbors.append(board[i,j])
	return sum(neighbors)

def tick(board_in):
	board_out = np.zeros(board_in.shape)
	n = board_in.shape
	for i in range(1,board_in.shape[0]-1):
		for j in range(1,board_in.shape[1]-1):
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

def play(rounds, board_size):
	board = np.zeros((board_size, board_size))
	for i in range(board_size):
		for j in range(board_size):
			board[i,j] = random.randint(0,1)
	
	for r in range(rounds):
		print (board)
		board = tick(board)
 
play(10, 10)
				
			


