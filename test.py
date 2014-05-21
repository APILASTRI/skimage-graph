import graph
import time
import sys

N = int(sys.argv[1])
g = graph.Graph(N)

T = time.time()
for i in range(N):
    g.make_edge(i,(i+1)%N,10*(i+1))

print "Constructing took %d s",time.time() - T

#g.draw('before.png')

for i in range(N-3):
    g.merge(i,i+1)
    

print "Merging took %d s",time.time() - T
#g.draw('after.png')
#g.display()
