import time
import numpy as np
import graph_csr as graph
from skimage import segmentation
import memory_profiler as mp




def test():
    arr = np.load("../data/watershed3.npy")
    arr = segmentation.relabel_sequential(arr)[0]
    t = time.time()
    
    base = mp.memory_usage()
    memory,g = mp.memory_usage((graph.construct_rag,(arr,),),interval = 0.01, retval = True, max_usage = True)
    
    #g = graph.construct_rag(arr)

    print "Memory for Construction =",memory[0] - base[0]
    
   # print "RAG construction took %f secs " % (time.time() - t)


    #exit()
    memory,g = mp.memory_usage((g.random_merge,(10,),),interval = 0.01, retval = True, max_usage = True)
    print "Memory for Merging =",memory[0] - base[0]

test()
