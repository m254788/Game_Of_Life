import pygame
pygame.init()

white = (255,255,255)
black = (0,0,0)
yellow = (255,255,0)



def make_grid(n,block_size):
	global disp
	global block_len
	block_len = block_size
	margin_size = 1
	grid_size = n+1+(n*block_size)
	disp = pygame.display.set_mode((grid_size,grid_size))
	disp.fill(white)
	for x in range(margin_size,grid_size,block_size+margin_size):
		for y in range(margin_size,grid_size,block_size+margin_size):
			rect = pygame.Rect(x, y, block_size, block_size)
			pygame.draw.rect(disp, black, [x,y,block_size,block_size])
	pygame.display.update()
def seed():
	pass


make_grid(10,30)
close_window  = False
start_game = False
while not close_window :
	for event in pygame.event.get():
		if event.type==pygame.QUIT:	
			close_window  = True
			break
			continue

		while not start_game:
			for event in pygame.event.get():
				if event.type==pygame.MOUSEBUTTONDOWN:
					pos = pygame.mouse.get_pos()
					x = pos[0]//block_len
					y = pos[1]//block_len
					
					
	
pygame.quit()
quit()


