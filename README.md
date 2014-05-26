skimage-graph
=============

A graph data structure for skimage. Intended for GSoC 2014

### Implemenetaion

* Each node holds a dictionary which maps adjacent nodes to their corresponding weihgts. Let's call this **Adjacency Dictionary**
* This approach is atleast `30x` faster than the last one
* Merging nodes is faster because lookup takes constant time.

### Further Imporovements
* Number of nodes in the graph need not remain constant. Therefore `Graph.rows` need not be a static never changing list. It can be a dictionary mapping vertex number to Adjacency Dictionary. Rather than keeping empty nodes, this will allow quick deletion of them.
* Node properties can be stored using a dictionary
* Edge properties can be stored by using a dictionary to map `(i,j) -> value`
* Each node will also contain a list of labels. If node `x` has label `1` and node `y` has label `2`. The new merged nodes label list will become `[1,2]`.


### Testing
```shell
> python test.py
```



## Results
###Speed

```bash
vighnesh@viggie-pc:skimage-graph > python test.py 
Edges =  39739
RAG Construction took 41.805317 s
Merging took 23.589030 s
(3485,3121) -> 1
(3817,3121) -> 1
(3817,3485) -> 1
(9868,3121) -> 1
(12695,3817) -> 1
(12695,3485) -> 1
(14658,3817) -> 1
(14658,3121) -> 1
(14658,3485) -> 1
(15038,14658) -> 1
(15038,3817) -> 1
(15038,3121) -> 1
(15038,3485) -> 1
(18004,3485) -> 1
(19279,3485) -> 1
```

###Memory 
```
Line #    Mem usage    Increment   Line Contents
================================================
     8   38.660 MiB    0.000 MiB   @profile
     9                             def test():
    10  516.410 MiB  477.750 MiB       arr = np.load("../data/watershed.npy")
    11  516.410 MiB    0.000 MiB       t = time.time()
    12  527.418 MiB   11.008 MiB       g = rag.construct_rag_3d(arr)
    13  527.422 MiB    0.004 MiB       print "Edges = ",g.edge_count
    14  527.422 MiB    0.000 MiB       print "RAG Construction took %f s" % (time.time() - t)
    15  527.422 MiB    0.000 MiB       t = time.time()
    16                                 
    17  527.062 MiB   -0.359 MiB       g.random_merge()
    18  527.062 MiB    0.000 MiB       print "Merging took %f s" % (time.time() - t)
    19  527.062 MiB    0.000 MiB       g.display()
```

