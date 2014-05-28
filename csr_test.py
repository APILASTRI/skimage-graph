import graph
import random
import sys
import os
import psutil as ps
from scipy import sparse
import numpy as np

N = int(sys.argv[1])
D = 10


arr = sparse.lil_matrix((N, N))

for i in range(N):
    for j in range(D):
        k = random.randint(0, N - 1)
        arr[i, k] = 1
        arr[k, i] = 1

csr = sparse.csr_matrix(arr)
del arr
prop_array = np.zeros((N,), dtype=int)


proc = ps.Process(os.getpid())
rss, vms = proc.get_memory_info()

print "RSS = %d MB" % (rss / 1000000)
print "VMS = %d MB" % (vms / 1000000)
