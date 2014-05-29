skimage-graph
=============



# Results
## Custom class

**Memory**
```
Line #    Mem usage    Increment   Line Contents
================================================
    13   18.176 MiB    0.000 MiB   @profile
    14                             def test():
    15  496.133 MiB  477.957 MiB       arr = np.load("../data/watershed.npy")
    16  496.133 MiB    0.000 MiB       t = time.time()
    17  507.359 MiB   11.227 MiB       g = graph.construct_rag(arr)
    18  507.363 MiB    0.004 MiB       print g.rows[1]
    19  507.371 MiB    0.008 MiB       print "RAG construction took %f secs " % (time.time() - t)
    20                             
    21  507.371 MiB    0.000 MiB       t = time.time()
    22  506.730 MiB   -0.641 MiB       g.random_merge(10)
    23                                 #g.display()
    24  506.730 MiB    0.000 MiB       print "Merging took %f secs " % (time.time() - t)
```


**Time**
```
RAG construction took 47.319908 secs 
Merging took 23.145860 secs 
```


