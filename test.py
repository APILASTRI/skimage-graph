import time
import numpy as np
import graph_csr as graph
from skimage import segmentation
import memory_profiler as mp
import cProfile


def test():
    arr = np.load("../data/watershed.npy")
    arr = segmentation.relabel_sequential(arr)[0]
    t = time.time()

    cProfile.runctx(
        "g = graph.construct_rag(arr)",
        globals(),
        locals(),
        "const.prof")

    cProfile.runctx(
        "g = g.random_merge(10)",
        globals(),
        locals(),
        "merge.prof")

    # print "Memory for Merging =",memory[0] - base[0]

test()
