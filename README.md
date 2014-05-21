skimage-graph
=============

A graph data structure for skimage. Intended for GSoC 2014

### Benchmarking
```shell
> python test.py number
```
where `number` in an integer.
The code will construct a cycle with n nodes and n edges, and keep merging edges till there are onyl 3 nodes left.


### Results

```shell
vighnesh@viggie-pc:skimage-graph > python test.py 10
Constructing took %d s 0.000922918319702
Merging took %d s 0.00173687934875
vighnesh@viggie-pc:skimage-graph > python test.py 100
Constructing took %d s 0.00857901573181
Merging took %d s 0.0186810493469
vighnesh@viggie-pc:skimage-graph > python test.py 1000
Constructing took %d s 0.0851612091064
Merging took %d s 0.19070315361
vighnesh@viggie-pc:skimage-graph > python test.py 10000
Constructing took %d s 0.852421998978
Merging took %d s 1.90656590462
vighnesh@viggie-pc:skimage-graph > python test.py 100000
Constructing took %d s 8.53914999962
Merging took %d s 19.268034935
```

When the degrees are small, merging one edge takes near constant time.
