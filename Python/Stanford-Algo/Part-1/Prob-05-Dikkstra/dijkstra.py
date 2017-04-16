__author__ = 'thale'

import random
import math
import copy

# To import the graph module, you deed to add the following path to import the lib from a different directory
import sys
sys.path.insert(0, '../../../Lib/Graphs/')
import Graphs


###########################################################################################################
# ReadGraphFromFile

debug_mode = True

def ReadGraphFromFile( fileName ):

    print "Name of the file: ", fileName
    first_header_line = True

    for line in open(fileName):
        print line
        edge = line.split()

        if first_header_line:
            first_header_line = False
            maxSize = int(edge[0])
            graphFromFile = Graphs.Graph(maxSize+1)
        else:
            vertex = int(edge[0])
            for next_vertex in edge:
                adjacent_vertex = next_vertex.split(',')
                #debug_var = (adjacent_vertex[0])
                if int(adjacent_vertex[0]) != vertex:
                    # Note, althought this graph isn't directed, each vertex has an adjacency list,
                    # so to prevent duplicates we call insert edge with directed = True to prevent
                    # that function from doing it both ways.

                    graphFromFile.InsertEdge(vertex, int(adjacent_vertex[0]), True, int(adjacent_vertex[1]) )

    return graphFromFile, maxSize


# End of file stuff
###########################################################################################################


###########################################################################################################
# dijkstra

def dijkstra(g, start, maxSize):

    # is the vertex in the tree yet?
    intree = [False]*(maxSize+1)
    # distance vertex is from start
    distance = [sys.maxint]*(maxSize+1)
    parent = [-1]*(maxSize+1)

    distance[start] = 0
    v = start

    while (intree[v] == False):
        intree[v] = True
        vertex_edge_list = g.vertices[v]
        for next_edge in vertex_edge_list.edges:
            w = next_edge.adjancentVertex
            weight = next_edge.weight
            if (distance[w] > (distance[v]+weight)):
                distance[w] = distance[v]+weight
                parent[w] = v

        v = 1
        dist = sys.maxint
        for i in range(1, len(g.vertices) ):
        	if ((intree[i] == False) and (dist > distance[i])):
        		dist = distance[i]
        		v = i
			

    for i in range(1, len(distance) ):
        print "distance for vertex is ", i, distance[i]


    # 2599,2610,2947,2052,2367,2399,2029,2442,2505,3068

#for (i=1 i<=g->nvertices i++) printf("%d %d\n",i,distance[i])*/


# End of dijkstra
###########################################################################################################


def main():
    #filename = "test_dijkstra.txt"
    #filename = "note_pad_P2_example.txt"
    filename = "dijkstraData.txt"

    graph, size = ReadGraphFromFile( filename )
    dijkstra(graph, 1, size)



if __name__ == '__main__':
    main()