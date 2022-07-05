import numpy as np
import sys
sys.path.insert(1,".")
import hdf5Helper as h5h

params = np.loadtxt("params.txt",dtype='int')
n = params[0]
rounds = params[1]

for r in range(rounds):
	dims = (1,n,n)
	board = np.loadtxt("evolution"+str(r)+".txt",dtype=np.float32).reshape(dims)
	dx = 1	
	#write to output data files
	h5_file = 'out'+str(r)+'.h5'
	xmf_file = 'data'+str(r)+'.xmf'
	h5h.writeH5_GOL(board, h5_file)
	h5h.writeXdmf_GOL(dims, dx, xmf_file, h5_file)





