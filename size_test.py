import graph
import random
import sys
import os
import psutil as ps


N = int(sys.argv[1])
D = 10


g = graph.Graph(N)

for i in range(N):
    for j in range(D):
        k = random.randint(0, N - 1)
        g.make_edge(i, k, 1)


proc = ps.Process(os.getpid())
rss, vms = proc.get_memory_info()

print "RSS = %d MB" % (rss / 1000000)
print "VMS = %d MB" % (vms / 1000000)
