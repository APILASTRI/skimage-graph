import graph
import time
import rag
import numpy as np
from skimage import io
from matplotlib import pyplot as plt

@profile
def test():
    arr = np.load("../data/watershed.npy")
    t = time.time()
    g = rag.construct_rag_3d(arr)
    print "Edges = ",g.edge_count
    print "RAG Construction took %f s" % (time.time() - t)
    t = time.time()
    
    g.random_merge()
    print "Merging took %f s" % (time.time() - t)
    g.display()

test()

