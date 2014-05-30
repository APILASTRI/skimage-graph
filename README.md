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

## Networx Graph Class

**Memory**
```
Line #    Mem usage    Increment   Line Contents
================================================
    12   23.023 MiB    0.000 MiB   @profile
    13                             def test():
    14  500.918 MiB  477.895 MiB       arr = np.load("../data/watershed.npy")
    15  500.918 MiB    0.000 MiB       t = time.time()
    16  530.703 MiB   29.785 MiB       g = graph.construct_rag(arr)
    17                                 
    18                                 
    19  530.719 MiB    0.016 MiB       print "RAG construction took %f secs " % (time.time() - t)
    20                             
    21  530.719 MiB    0.000 MiB       t = time.time()
    22  517.906 MiB  -12.812 MiB       g.random_merge(10)
    23                                 #g.display()
    24  517.906 MiB    0.000 MiB       print "Merging took %f secs " % (time.time() - t)

```

**Time**
```
RAG construction took 117.332280 secs 
Merging took 1.238992 secs
```
