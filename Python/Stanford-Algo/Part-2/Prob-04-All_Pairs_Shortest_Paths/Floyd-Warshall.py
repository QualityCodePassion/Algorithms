#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      t.hale
#
# Created:     24/07/2014
# Copyright:   (c) t.hale 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import sys
import time

###########################################################################################################
#   TODO Put this into the GraphFile module
###########################################################################################################

def ReadPriorityWeightedMatrixFromFile( fileName ):

    print "Name of the file: ", fileName
    firstLine = True

    for line in open(fileName):
        if( firstLine ):
            print line
            edge = line.split()
            numberOfVertices = int(edge[0])
            matrix_lenght = numberOfVertices + 1
            firstLine = False

            print "Start 1 init = ", time.clock()
            A = []
            for i in range(matrix_lenght):
                B = []
                for j in range(matrix_lenght):
                    C = [sys.maxint]*(matrix_lenght)
                    B.append(C)
                A.append(B)
            print "End 1 init = ", time.clock()

            print "Start 2 init = ", time.clock()
            for i in range(1, matrix_lenght):
                for j in range(1, matrix_lenght):
                    if i == j:
                        A[i][j][0] = 0
##                        else:
##                            # This is init to infinity, but it gets set to the edge
##                            # weight when reading the file if an edge exists
##                            A[i][j][0] = test = int("inf")
            print "End 2 init = ", time.clock()

        else:
            #print line
            edge = line.split()
            A[int(edge[0])][int(edge[1])][0] = int(edge[2])

    return A, numberOfVertices

###########################################################################################################



def Floyd_Warshall(A, numberOfVertices, graph_number ):

    matrix_lenght = numberOfVertices + 1
    start_time = time.clock()
    previous_time = start_time
    print "Start Floyd_Warshall = ", start_time

    for k in range(1, matrix_lenght):
        print "loop and Accumulated time, k and graph number = ", (time.clock() - previous_time), (time.clock() - start_time), k, graph_number
        previous_time = time.clock()

        for i in range(1, matrix_lenght):
            for j in range(1, matrix_lenght):
                A[i][j][k] = min( A[i][j][k-1], A[i][k][k-1] + A[k][j][k-1] )

    # Note, when k = matrix_lenght, these are all the shortest paths.
    # Therefore, we can just need to find the smallest value for k = matrix_lenght

    finish_time = time.clock()
    print "Start time was = ", start_time
    print "End Floyd_Warshall = ", finish_time
    print "Algorithm took = " , (finish_time - start_time)

    shortest_paths = []
    for i in range(1, matrix_lenght):
        for j in range(1, matrix_lenght):
            if i == j:
                # Check for a negative cycle (i.e. a negative value on the diaganol of final solution
                if A[i][i][numberOfVertices] < 0:
                    print "Error, this graph has a negative cycle!"
                    return sys.maxint
            else:
                shortest_paths.append(A[i][j][numberOfVertices])

    shortest_paths.sort()
    shortest_shortest_path = shortest_paths[0]

    print "Shortest path for graph ", graph_number
    print "is = ", shortest_shortest_path

    return shortest_shortest_path


def main():
##    matrixFromFile, numberOfVertices = ReadPriorityWeightedMatrixFromFile("test_floyd_edges.txt")
##    Floyd_Warshall( matrixFromFile, numberOfVertices, 1 )

    matrixFromFile1, numberOfVertices = ReadPriorityWeightedMatrixFromFile("g1.txt.bak")
    shortest_path1 = Floyd_Warshall( matrixFromFile1, numberOfVertices, 1 )

    shortest_path = shortest_path1
    shortest_graph = 1

##    matrixFromFile2, numberOfVertices = ReadPriorityWeightedMatrixFromFile("g2.txt.bak")
##    shortest_path2 = Floyd_Warshall( matrixFromFile2, numberOfVertices, 2 )
##
##    if shortest_path2 < shortest_path:
##        shortest_path = shortest_path2
##        shortest_graph = 2

    matrixFromFile3, numberOfVertices = ReadPriorityWeightedMatrixFromFile("g3.txt.bak")
    shortest_path3 = Floyd_Warshall( matrixFromFile3, numberOfVertices, 3 )

    if shortest_path3 < shortest_path:
        shortest_path = shortest_path3
        shortest_graph = 3

    print "Shortest shortest path is = ", shortest_path
    print "Which was on graph ", shortest_graph
    print "All shortest paths = ", shortest_path1, shortest_path3

if __name__ == '__main__':
    main()
