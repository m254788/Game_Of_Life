import numpy as np
import sys
board1 = np.loadtxt("cuda_evolution100.txt", dtype='int')
board2 = np.loadtxt("cpp_evolution100.txt", dtype='int')

success = True
for i in range(100*100):
    if board1[i] != board2[i]:
        success = False
        print(i)
        break

print(success)
