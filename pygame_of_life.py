import pygame
import numpy as np
import time
import random

pygame.init()
white = (255,255,255)
black = (0,0,0)
yellow = (255,255,0)

n = 100 #nxn grid
block_size = 7 #block_size
margin_size = 1 #fixed at 1

data = np.zeros((n,n))
for r in range(n):
	for c in range(n):
		data[r][c] = random.randint(0,1)
disp_size = n+1+(n*block_size) #pixel dim of display
disp=pygame.display.set_mode((disp_size,disp_size))
disp.fill(white)


def draw_cell(row,col,alive):
	if alive:
		pygame.draw.rect(disp,yellow,[margin_size+(margin_size+block_size)*col,margin_size+(margin_size+block_size)*row,block_size,block_size])
	else:
		pygame.draw.rect(disp,black,[margin_size+(margin_size+block_size)*col,margin_size+(margin_size+block_size)*row,block_size,block_size])
def update_disp_with_data():
	for row in range(n):
		for col in range(n):
			draw_cell(row,col,data[row][col])
			
	pygame.display.update()


def toggle_alive(row,col):
	data[row][col] = 1-data[row][col]

update_disp_with_data() #initialize board with all cells dead




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



game_over = False
go = False
while not go:
	for event in pygame.event.get():

		if event.type==pygame.MOUSEBUTTONDOWN:
			pos = pygame.mouse.get_pos()
			row = pos[1]//(margin_size+block_size) 
			col = pos[0]//(margin_size+block_size)
			toggle_alive(row,col)
			print(data)
			update_disp_with_data()

		elif event.type==pygame.KEYDOWN and event.key==pygame.K_SPACE:
			go = True

data = tick(data)
update_disp_with_data()
while go:
	data = tick(data)
	update_disp_with_data()
	time.sleep(0.2)
	
	
pygame.quit()
quit()					

