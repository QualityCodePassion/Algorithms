#-------------------------------------------------------------------------------
# Name:        Graphs
# Purpose:
#
# Author:      t.hale
#
# Created:     23/06/2014
# Copyright:   (c) t.hale 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------


# To import this module, you deed to add the following path to import the lib from a different directory
#import sys
#sys.path.insert(0, '../Lib/Graphs/')
#import Graphs


class Edge:
    def __init__(self, y, w):
        self.adjancentVertex = y
        self.weight = w

class EdgeList:
    def __init__(self):
        self.edges = []

    def InsertEdge(self, y, w):
        self.edges.append( Edge(y,w))

class Graph(object):
    def __init__(self, maxSize, directed = False):
        print "init graph with max size of ", maxSize
        self.directed = directed

        # initialize the list (can't use the "*" opertor for this because it only does shallow
        # copies pointing to the same "EdgeList" object.
        self.vertices = []
        for i in range(0, maxSize):
            self.vertices.append(EdgeList())

    def InsertEdge( self, x,y, directed = False, weight = 0 ):
        vertex = self.vertices[x]
        vertex.InsertEdge(y, weight)
        if( not directed ):
            self.InsertEdge( y, x, True, weight)

# End of graph stuff
###########################################################################################################


def main():
    pass

if __name__ == '__main__':
    main()
