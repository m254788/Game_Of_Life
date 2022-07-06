import numpy as np
import sys
board1 = np.loadtxt("board1.txt", dtype='int')
board2 = np.loadtxt("board2.txt", dtype='int')

success = True
for i in range(100*100):
    if board1[i] != board2[i]:
        success = False
        print(i)
        break

print(success)
