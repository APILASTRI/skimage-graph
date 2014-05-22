import graph
import time
import sys

N = int(sys.argv[1])
g = graph.Graph(N)

T = time.time()
for i in range(N):
    g.make_edge(i,(i+1)%N,10*(i+1))

#g.make_edge(0,2,99)
#g.merge(0,2)

print "Constructing took %f s" % (time.time() - T)

#g.draw('before.png')

for i in range(N-3):
    g.merge(i,i+1)
    

print "Merging took %f s" % (time.time() - T)
#g.draw('graph.png')
#g.display()
