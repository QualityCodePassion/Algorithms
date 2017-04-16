__author__ = 'thale'

import random
import math
import copy

# To import the graph module, you deed to add the following path to import the lib from a different directory
import sys
sys.path.insert(0, '../../../Lib/Graphs/')
import Contractable_Graphs


###########################################################################################################
# ReadGraphFromFile

debug_mode = False

def ReadGraphFromFile( fileName ):

    print "Name of the file: ", fileName
    first_header_line = True

    for line in open(fileName):
        print line
        edge = line.split()

        if first_header_line:
            first_header_line = False
            maxSize = int(edge[0])
            graphFromFile = Graphs.Contracted_Graph(maxSize)
        else:
            vertex = int(edge[0])
            for adjacent_vertex in edge:
                if int(adjacent_vertex) != vertex:
                    # Note, althought this graph isn't directed, each vertex has an adjacency list,
                    # so to prevent duplicates we call insert edge with directed = true to prevent
                    # that function from doing it both ways.
                    graphFromFile.InsertEdge(vertex, int(adjacent_vertex), True)

    return graphFromFile, maxSize


# End of file stuff
###########################################################################################################



def main():
    filename = "kargerMinCut.txt"
    #filename = "TestContraction.txt"
    #filename = "TestContraction_2.txt"

    graph, size = ReadGraphFromFile( filename )

    init_graph = copy.deepcopy(graph)

    smallest_number_of_crossing_edges = sys.maxint - 1
    number_of_trials = int( size*size*math.log1p(size) )
    for i in range(0, number_of_trials):
        # reset the graph for another trial
        graph = copy.deepcopy(init_graph)
        still_contracting_graph = True
        while still_contracting_graph:
            still_contracting_graph = graph.contract_vertices()

        current_crossing_edges_count = graph.count_crossing_edges()
        if debug_mode:
            print "Current crossind edges = ", current_crossing_edges_count

        if current_crossing_edges_count < smallest_number_of_crossing_edges:
            smallest_number_of_crossing_edges = current_crossing_edges_count
            print "new smallest = ", smallest_number_of_crossing_edges

    print "Smallest Number of crossing edges = ", smallest_number_of_crossing_edges



if __name__ == '__main__':
    main()