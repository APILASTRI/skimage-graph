skimage-graph
=============

A graph data structure for skimage. Intended for GSoC 2014

### Benchmarking
```shell
> python test.py n
```
where `n` in an integer.
The code will construct a cycle with `n` nodes and `n` edges, and keep merging edges till there are only 3 nodes left.


### Results

```shell
vighnesh@viggie-pc:skimage-graph > python test.py 10
Constructing took 0.000924 s
Merging took 0.001806 s
vighnesh@viggie-pc:skimage-graph > python test.py 100
Constructing took 0.008928 s
Merging took 0.020233 s
vighnesh@viggie-pc:skimage-graph > python test.py 1000
Constructing took 0.086023 s
Merging took 0.191397 s
vighnesh@viggie-pc:skimage-graph > python test.py 10000
Constructing took 0.849043 s
Merging took 1.884101 s
vighnesh@viggie-pc:skimage-graph > python test.py 100000
Constructing took 8.294484 s
Merging took 18.534647 s
```

When the degrees are small, merging one edge takes near constant time.
