import time
import numpy as np
import graph_csr as graph


try:
    profile
except NameError:
    def profile(x):
        return x


@profile
def test():
    arr = np.load("../data/watershed.npy")
    t = time.time()
    g = graph.construct_rag(arr)

    print "RAG construction took %f secs " % (time.time() - t)

    #print g.max_size
    t = time.time()
    g.random_merge(10)
    #print g.max_size
    print "Merging took %f secs " % (time.time() - t)


test()
