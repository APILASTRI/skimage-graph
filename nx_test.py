import networkx as nx
import random
import sys
import os
import psutil as ps


N = int(sys.argv[1])
D = 10


g = nx.Graph()

for i in range(N):
    for j in range(D):
        k = random.randint(0, N - 1)
        g.add_edge(i, k, weight=1)
        g.edge[i][k]['prop'] = 100


proc = ps.Process(os.getpid())
rss, vms = proc.get_memory_info()

print "RSS = %d MB" % (rss / 1000000)
print "VMS = %d MB" % (vms / 1000000)
