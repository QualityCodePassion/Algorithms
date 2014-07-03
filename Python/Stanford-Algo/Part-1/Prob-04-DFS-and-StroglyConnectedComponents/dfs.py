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

import collections

# To import this module, you deed to add the following path to import the lib from a different directory
import sys
sys.path.insert(0, '../../../Lib/Graphs/')
import Graphs

#import os, sys
#lib_path = os.path.abspath('../../../Lib/Graphs/')
#sys.path.append(lib_path)


maxGraphSize = 100;


###########################################################################################################
# TODO put the following into the File modules


def ReadGraphFromFile( fileName, maxSize ):

    print "Name of the file: ", fileName
    graphFromFile = Graphs.Graph(maxSize)
    for line in open(fileName):
        print line
        edge = line.split()
        graphFromFile.InsertEdge(int(edge[0]), int(edge[1]))

    return graphFromFile


# End of file stuff
###########################################################################################################


###########################################################################################################
# TODO put the following DFS into it's own class then into the graph modules

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

# end of DFS
###########################################################################################################


###########################################################################################################
# TODO put the following BFS into it's own class then into the graph modules

vertexQueue = collections.deque()
discovered = [False]*maxGraphSize
processed = [False]*maxGraphSize
parent = [0]*maxGraphSize

def ProcessVertexEarly( vertex ):
    print("process vertex early: ", vertex)

def ProcessVertexLate( vertex ):
    #print("process vertex late: ", vertex)
    pass

def ProcessEdge( x, y ):
    print("Process edge:", x , y)


def BFS( graph, start ):
    discovered[start] = True
    print "starting at vertex", start
    vertexQueue.append(start)

    # pop each element off queue until it's empty
    while( vertexQueue ):
        vertex = vertexQueue.popleft()
        ProcessVertexEarly( vertex )
        processed[vertex] = True

        # Get all the edges for this vertex and iterate over them all
        edgeList = graph.vertices[vertex]
        for edge in edgeList.edges:
            nextVertex = edge.adjancentVertex

            if ( (not processed[nextVertex]) or graph.directed):
                ProcessEdge( vertex, nextVertex )

            if( not discovered[nextVertex]):
                discovered[nextVertex] = True
                #put next vertex onto a queue
                vertexQueue.append(nextVertex)
                parent[nextVertex] = vertex

        ProcessVertexLate(vertex)


# end of BFS
###########################################################################################################



def main():
    graphFromFile = ReadGraphFromFile("../Data/DummyGraphEdges.txt", maxGraphSize)
    #DFS(graphFromFile, 1)

    BFS(graphFromFile, 1)

    #testGraph = Graphs.Graph(10)
    #testGraph.InsertEdge(1,7)

if __name__ == '__main__':
    main()
