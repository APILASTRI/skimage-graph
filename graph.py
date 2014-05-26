import numpy as np
import pygraphviz as pgv


class Graph(object):

    def __init__(self, n):

        # TODO : Why shoukd this be a list, can't this be a dict as well
        # Number of vertices do not remain the same
        self.rows = [{} for i in range(n)]

    def display(self):
        for i in range(len(self.rows)):
            for key in self.rows[i]:
                if key < i:
                    print "(%d,%d) -> %d" % (i, key, self.rows[i][key])

    def make_edge(self, i, j, wt):
        self.rows[i][j] = wt
        self.rows[j][i] = wt

    def merge(self, i, j):
        # we merge i into j and delete the contents of i

        # Checking if nodes are adjacent
        try:
            self.rows[j][i]
        except KeyError:
            # catching one error to throw another, does this make sense ?
            raise ValueError("Whoa Bro ! You can't merge non adjacent nodes.")

        # this is the dictionary for the new node,
        # first, copy the contents of i
        nd = self.rows[i].copy()

        # append contents of j, and replace when higher weight comes from j
        [nd.__setitem__(k, v)
         for k, v in self.rows[j].viewitems() if v > nd.get(k, -1)]

        # new node won't be adjacent to i or j
        del nd[i]
        del nd[j]

        # nd now has the proper contents
        # update other nodes according to nd

        # delete i from nodes adjacent to i
        [self.rows[k].__delitem__(i) for k in self.rows[i].keys()]

        # update the weights for nodes adjacent to the new node
        [self.rows[k].__setitem__(j, v) for k, v in nd.viewitems()]

        self.rows[i] = {}
        self.rows[j] = nd

    def draw(self, name):
        g = pgv.AGraph()

        for i in range(len(self.rows)):
            for key in self.rows[i]:
                if key < i:
                    g.add_edge(i, key)
                    e = g.get_edge(i, key)
                    e.attr['label'] = str(self.rows[i][key])

        g.layout('circo')
        g.draw(name)
