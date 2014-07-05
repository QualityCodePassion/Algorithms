#-------------------------------------------------------------------------------
# Name:        Prims
# Purpose:
#
# Author:      t.hale
#
# Created:     03/07/2014
# Copyright:   (c) t.hale 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# To import the graph module, you deed to add the following path to import the lib from a different directory
import sys
# sys.path.insert(0, '../../../Lib/') This didn't work when I tried doing a "from Lib.FileIO.GraphFile imort Graphs"
sys.path.insert(0, '../../../Lib/FileIO/')
sys.path.insert(0, '../../../Lib/Graphs/')
sys.path.insert(0, '../../../Lib/DataStructures/')

import heapq

import Graphs
from GraphFile import ReadWeightedGraphFromFile
from PriorityQueue import PriorityQueue



###########################################################################################################
#   TODO Put this into the GraphFile module and put replace "PriorityGraph" with "Graphs.PriorityGraph"
###########################################################################################################

def ReadPriorityWeightedGraphFromFile( fileName ):

    print "Name of the file: ", fileName
    firstLine = True

    for line in open(fileName):
        if( firstLine ):
            print line
            edge = line.split()
            numberOfVertices = int(edge[0]) + 1
            graphFromFile = PriorityGraph(numberOfVertices)
            firstLine = False
        else:
            #print line
            edge = line.split()
            graphFromFile.InsertEdge(int(edge[0]), int(edge[1]), False, int(edge[2]) )

    return graphFromFile

###########################################################################################################



###########################################################################################################
# Weighted Priority (Heap) Graph

# TODO Put this into the Graphs module

# TODO  PriorityGraph is identical to a normal graph except it inserts into a priorityEdgeList,
#       So I could use "duck typing" inheritence or just a flag in the init to say what type it is

###########################################################################################################


class PriorityEdgeList:
    def __init__(self):
        self.edges = []
        self.priorityEdges = PriorityQueue()
        self.empty = True

    def InsertEdge(self, y, w):
        self.priorityEdges.add_task(y, w)
        self.edges.append( Graphs.Edge(y,w))
        self.empty = False

class PriorityGraph(object):
    def __init__(self, maxVertices, directed = False):
        print "init graph with max size of ", maxVertices
        self.directed = directed
        self.maxVertices = maxVertices

        # initialize the list (can't use the "*" opertor for this because it only does shallow
        # copies pointing to the same "EdgeList" object.
        self.vertices = []
        for i in range(0, maxVertices):
            self.vertices.append(PriorityEdgeList())

    def InsertEdge( self, x,y, directed = False, weight = 0 ):
        vertex = self.vertices[x]
        vertex.InsertEdge(y, weight)
        if( not directed ):
            self.InsertEdge( y, x, True, weight)

# End of Weighted Priority Graph
###########################################################################################################


###########################################################################################################
# Prims
###########################################################################################################

def Prims( graph, start ):
    ''' Creates a minimum  spanning tree using Prims algorithm
    '''
    print "Start vertex = ", start

    spanningTree = Graphs.Graph( graph.maxVertices, False )
    inTree = [False]*graph.maxVertices
    inTree[start] = True
    spanningVertices = []   #[0]*graph.maxVertices
    spanningVertices.append(start)

    # Initialize the heap (PriorityQueue) with the min edge of the first
    # vertex for its key, and ininity for all other keys (vertexs).
    heapQueue = PriorityQueue()
#    for vertex in range(0, len(graph.vertices)):
#        if( not (graph.vertices[vertex]).empty ):
#            heapQueue.add_task(vertex, sys.maxint)

    startEdges = (graph.vertices[start]).priorityEdges
    nextVertex, minWeight, noMoreValidEdges = startEdges.pop_task()
    heapQueue.add_task( (start, nextVertex), minWeight)
    totalCost = 0


    while( not noMoreValidEdges ):

        # Pop the next cheapest edge off the list off the heap (prioirty queue) (this will remove it)
        nextEdge, cheapestWeight, noMoreValidEdges = heapQueue.pop_task()

        if( not noMoreValidEdges ):
            nextVertex = nextEdge[1]
            vertexInTreeGettingUpdate = nextEdge[0]
            if( not inTree[nextVertex] ):
                print "Next vertex and weight = ", nextVertex, cheapestWeight
                totalCost += cheapestWeight
                inTree[nextVertex] = True
                spanningVertices.append(nextVertex)
                spanningTree.InsertEdge(vertexInTreeGettingUpdate, nextVertex, False, cheapestWeight)

                # Need to find the cheapest edges for both vertex's on the next edge that is
                # coming into the spanning tree.
                # Note that the edge that led to this vertex being selected has now been
                # removed from the "priorityEdges" for that vertex by the "pop_task()" function below
                nextEdges = (graph.vertices[nextVertex]).priorityEdges
                edgesEmpty = False
                cheapestEdgeVertex = nextVertex
                # We keep popping the edges until we find one that's not already in the tree.
                while( (not edgesEmpty) and (inTree[cheapestEdgeVertex])):
                    cheapestEdgeVertex, cheapestEdgeWeight, edgesEmpty = nextEdges.pop_task()
                if( not edgesEmpty ):
                    heapQueue.add_task((nextVertex, cheapestEdgeVertex), cheapestEdgeWeight)

                nextEdges = (graph.vertices[vertexInTreeGettingUpdate]).priorityEdges
                edgesEmpty = False
                cheapestEdgeVertex = vertexInTreeGettingUpdate
                # We keep popping the edges until we find one that's not already in the tree.
                while( (not edgesEmpty) and (inTree[cheapestEdgeVertex])):
                    cheapestEdgeVertex, cheapestEdgeWeight, edgesEmpty = nextEdges.pop_task()
                if( not edgesEmpty ):
                    heapQueue.add_task( (vertexInTreeGettingUpdate, cheapestEdgeVertex), cheapestEdgeWeight)

    return totalCost


def main():
    #graphFromFile = ReadPriorityWeightedGraphFromFile("prims_edges.txt.bak")
    graphFromFile = ReadPriorityWeightedGraphFromFile("test_prims_edges_02.txt")
    start = 1
    totalCost = Prims(graphFromFile, start)
    print "Total Cost = ", totalCost

if __name__ == '__main__':
    main()
