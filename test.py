import time
import numpy as np
import graph_custom as graph



try :
    profile
except NameError:
    def profile(x):
        return x


def test():
    arr = np.load("../data/watershed.npy")
    t = time.time()
    g = graph.construct_rag(arr)
    t = time.time()

    g.random_merge(10)
    g.display()

test()
