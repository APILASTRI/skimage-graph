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
> python test.py n
```
where `n` in an integer.
The code will construct a cycle with `n` nodes and `n` edges, and keep merging edges till there are only 3 nodes left.


## Results
###Speed

```bash
vighnesh@viggie-pc:skimage-graph > python test.py 10
Constructing took 0.000020 s
Merging took 0.000207 s
vighnesh@viggie-pc:skimage-graph > python test.py 100
Constructing took 0.000055 s
Merging took 0.000457 s
vighnesh@viggie-pc:skimage-graph > python test.py 1000
Constructing took 0.000551 s
Merging took 0.004031 s
vighnesh@viggie-pc:skimage-graph > python test.py 10000
Constructing took 0.005496 s
Merging took 0.041347 s
vighnesh@viggie-pc:skimage-graph > python test.py 100000
Constructing took 0.057140 s
Merging took 0.409411 s
vighnesh@viggie-pc:skimage-graph > python test.py 1000000
Constructing took 0.568724 s
Merging took 4.164443 s
```

###Memory - 10 Nodes
```
Filename: graph.py

Line #    Mem usage    Increment   Line Contents
================================================
    22   18.109 MiB    0.000 MiB       @profile
    23                                 def make_edge(self,i,j,wt):
    24   18.109 MiB    0.000 MiB           self.rows[i][j] = wt
    25   18.109 MiB    0.000 MiB           self.rows[j][i] = wt


Filename: graph.py

Line #    Mem usage    Increment   Line Contents
================================================
    27   18.129 MiB    0.000 MiB       @profile
    28                                 def merge(self,i,j):
    29                                     # we merge i into j and delete the contents of i
    30                             
    31                                     #Checking if nodes are adjacent
    32   18.129 MiB    0.000 MiB           try :
    33   18.129 MiB    0.000 MiB               self.rows[j][i]
    34                                     except KeyError :
    35                                         # catching one error to throw another, does this make sense ?
    36                                         raise ValueError("Whoa Bro ! You can't merge non adjacent nodes.")
    37                             
    38                                     # this is the dictionary for the new node,
    39                                     # first, copy the contents of i
    40   18.129 MiB    0.000 MiB           nd = self.rows[i].copy()
    41                             
    42                                     # append contents of j, and replace when higher weight comes from j
    43   18.129 MiB    0.000 MiB           [ nd.__setitem__(k, v) for k, v in self.rows[j].viewitems() if v > nd.get(k,-1) ]
    44                             
    45                                     # new node won't be adjacent to i or j
    46   18.129 MiB    0.000 MiB           del nd[i]
    47   18.129 MiB    0.000 MiB           del nd[j]
    48                             
    49                                     # nd now has the proper contents
    50                                     # update other nodes according to nd
    51                             
    52                                     # delete i from nodes adjacent to i
    53   18.129 MiB    0.000 MiB           [ self.rows[k].__delitem__(i) for k in self.rows[i].keys() ]
    54                                     
    55                                     # update the weights for nodes adjacent to the new node
    56   18.129 MiB    0.000 MiB           [ self.rows[k].__setitem__(j, v) for k,v in nd.viewitems() ]
    57                             
    58   18.129 MiB    0.000 MiB           self.rows[i] = {}
    59   18.129 MiB    0.000 MiB           self.rows[j] = nd


Filename: graph.py

Line #    Mem usage    Increment   Line Contents
================================================
     9   18.109 MiB    0.000 MiB       @profile
    10                                 def __init__(self,n):
    11                             
    12                                     # TODO : Why shoukd this be a list, can't this be a dict as well
    13                                     # Number of vertices do not remain the same
    14   18.109 MiB    0.000 MiB           self.rows = [{} for i in range(n)]
```

###Memory 10000 Nodes
When the degrees are small, merging one edge takes near constant time.
```
Line #    Mem usage    Increment   Line Contents
================================================
    22   21.633 MiB    0.000 MiB       @profile
    23                                 def make_edge(self,i,j,wt):
    24   21.633 MiB    0.000 MiB           self.rows[i][j] = wt
    25   21.633 MiB    0.000 MiB           self.rows[j][i] = wt


Filename: graph.py

Line #    Mem usage    Increment   Line Contents
================================================
    27   21.883 MiB    0.000 MiB       @profile
    28                                 def merge(self,i,j):
    29                                     # we merge i into j and delete the contents of i
    30                             
    31                                     #Checking if nodes are adjacent
    32   21.883 MiB    0.000 MiB           try :
    33   21.883 MiB    0.000 MiB               self.rows[j][i]
    34                                     except KeyError :
    35                                         # catching one error to throw another, does this make sense ?
    36                                         raise ValueError("Whoa Bro ! You can't merge non adjacent nodes.")
    37                             
    38                                     # this is the dictionary for the new node,
    39                                     # first, copy the contents of i
    40   21.883 MiB    0.000 MiB           nd = self.rows[i].copy()
    41                             
    42                                     # append contents of j, and replace when higher weight comes from j
    43   21.883 MiB    0.000 MiB           [ nd.__setitem__(k, v) for k, v in self.rows[j].viewitems() if v > nd.get(k,-1) ]
    44                             
    45                                     # new node won't be adjacent to i or j
    46   21.883 MiB    0.000 MiB           del nd[i]
    47   21.883 MiB    0.000 MiB           del nd[j]
    48                             
    49                                     # nd now has the proper contents
    50                                     # update other nodes according to nd
    51                             
    52                                     # delete i from nodes adjacent to i
    53   21.883 MiB    0.000 MiB           [ self.rows[k].__delitem__(i) for k in self.rows[i].keys() ]
    54                                     
    55                                     # update the weights for nodes adjacent to the new node
    56   21.883 MiB    0.000 MiB           [ self.rows[k].__setitem__(j, v) for k,v in nd.viewitems() ]
    57                             
    58   21.883 MiB    0.000 MiB           self.rows[i] = {}
    59   21.883 MiB    0.000 MiB           self.rows[j] = nd


Filename: graph.py

Line #    Mem usage    Increment   Line Contents
================================================
     9   18.109 MiB    0.000 MiB       @profile
    10                                 def __init__(self,n):
    11                             
    12                                     # TODO : Why shoukd this be a list, can't this be a dict as well
    13                                     # Number of vertices do not remain the same
    14   21.219 MiB    3.109 MiB           self.rows = [{} for i in range(n)]
```

