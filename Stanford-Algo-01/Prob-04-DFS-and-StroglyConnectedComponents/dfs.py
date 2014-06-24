#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      t.hale
#
# Created:     22/06/2014
# Copyright:   (c) t.hale 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------


maxGraphSize = 100;


###########################################################################################################
# Todo uncooment the import below and put the graph staff in a module

# Need to add the following path to import the lib from a different directory
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
    def __init__(self, maxSize):
        print "init graph with max size of ", maxSize

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


###########################################################################################################
# TODO put the following into the File modules


def ReadGraphFromFile( fileName, maxSize ):

    print "Name of the file: ", fileName
    graphFromFile = Graph(maxSize)
    for line in open(fileName):
        print line
        edge = line.split()
        graphFromFile.InsertEdge(int(edge[0]), int(edge[1]))

    return graphFromFile


# End of file stuff
###########################################################################################################


###########################################################################################################
# TODO put the following into it's own class then into the graph modules

explored = [False]*maxGraphSize

def DFS( graph, start):
    explored[start] = True
    print "exploring vertex", start
    # Get all the edges on the "start" vertex
    edgeList = graph.vertices[start]

    for edge in edgeList.edges:
        nextVertex = edge.adjancentVertex

        if( not explored[nextVertex]):
            DFS(graph,nextVertex)
            print "finished exploring vertex", nextVertex



def main():
    graphFromFile = ReadGraphFromFile("../Data/DummyGraphEdges.txt", maxGraphSize)
    DFS(graphFromFile, 1)

    #testGraph = Graph(10)
    #testGraph.InsertEdge(1,7)

if __name__ == '__main__':
    main()
