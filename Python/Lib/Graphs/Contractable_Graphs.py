#-------------------------------------------------------------------------------
# Name:        Contractable_Graphs.py
# Purpose:
#
# Author:      t.hale
#
# Created:     23/06/2014
# Copyright:   (c) t.hale 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import random
import copy

# To import this module, you deed to add the following path to import the lib from a different directory
#import sys
#sys.path.insert(0, '../Lib/Graphs/')
#import Graphs

###########################################################################################################
# Standard graph (Can be weighted or not)

#class Edge:
#    def __init__(self, y, w):
#        self.adjancentVertex = y
#        self.weight = w

debug_mode = True

class EdgeList:
    def __init__(self, x):
        self.start_vertex = x
        self.parent_vertex = x
        self.edges = []
        self.initial_edges = []
        self.available_edges = []
        self.weights = []
        self.contracted_vertexs = []
        self.empty = True

    def InsertEdge(self, y, w):
        #self.edges.add_task(y, w)
        self.edges.append( y )
        self.available_edges.append( y )
        self.initial_edges.append( y )
        self.weights.append(w)
        self.empty = False


    def Contract(self, other_edge, other_vertices):
        other_edge_list = other_edge.edges

        #contract the other_vertices
        self.contracted_vertexs.extend(other_vertices)
        if self.start_vertex in self.contracted_vertexs:
            print "vertex ", self.start_vertex
            print "should be in its own contracted list ", self.contracted_vertexs

        in_first = set(self.edges)
        in_second = set(other_edge_list) - set( [self.start_vertex] )

        in_second_but_not_in_first = in_second - in_first
        append_edges = list(in_second_but_not_in_first)

        if append_edges:
            # append any newly gained edges
            self.edges.extend(append_edges)
            # Don't include the contracted vertices in the available_edges list

        self.available_edges = list( set(self.edges) - set(self.contracted_vertexs) )

        return True


class Graph(object):
    def __init__(self, maxVertices, directed = False):
        print "init graph with max size of ", maxVertices
        self.directed = directed
        self.maxVertices = maxVertices

        # initialize the list (can't use the "*" opertor for this because it only does shallow
        # copies pointing to the same "EdgeList" object.
        self.vertices = []
        for i in range(0, maxVertices + 1 ):
            self.vertices.append(EdgeList(i))

    def InsertEdge( self, x, y, directed = False, weight = 0 ):
        vertex = self.vertices[x]
        vertex.InsertEdge(y, weight)
        if( not directed ):
            self.InsertEdge( y, x, True, weight)

        if debug_mode:
            print "insert edge with weight", x, y, weight


# End of graph
###########################################################################################################

class Contracted_Graph(Graph):
    def __init__(self, maxVertices, directed = False):
        Graph.__init__(self, maxVertices, directed)
        print "init Contracted_Graph with max size of ", maxVertices
        #self.directed = directed
        #self.maxVertices = maxVertices
        self.available_vertices = range(1, maxVertices + 1)

    #def num_contracted_vertices(self):

    def contract_vertices(self):
        # return false when there are only 2 vertices available
        if len(self.available_vertices) <= 2:
            return False

        # randomly choose one vertex of the available vertices to contract with another
        random_index_1 = random.randrange(0, len(self.available_vertices) )
        if random_index_1 > len(self.available_vertices) - 1:
            raise "random when out of available range!"

        random_vertex_1 = self.available_vertices[random_index_1]
        edges_of_random_vertex_1 = self.vertices[random_vertex_1]
        # remove it from the list of available vertices
        self.available_vertices.remove( random_vertex_1 )

        # now choose one of its available adjacent vertices (i.e. one that hasn't already been contracted) at random
        # first need to update the available edges for the chosen vertex
        if debug_mode:
            print "random_vertex_1, edges_of_random_vertex_1.contracted_vertexs, edges_of_random_vertex_1.available_edges", random_vertex_1, edges_of_random_vertex_1.contracted_vertexs, edges_of_random_vertex_1.available_edges
            print "self.available_vertices", self.available_vertices
        remove_unavailable_vertices = []
        for i in edges_of_random_vertex_1.available_edges:
            if debug_mode:
                print "iterator ", i
            if i in edges_of_random_vertex_1.contracted_vertexs:
                remove_unavailable_vertices.append(i)
                if debug_mode:
                    print "removing unvailable edge ", i

        if remove_unavailable_vertices:
            for i in remove_unavailable_vertices:
                edges_of_random_vertex_1.available_edges.remove(i)

        if len(edges_of_random_vertex_1.available_edges) == 0:
            print "Need to fix this!"

        random_index_2 = random.randrange(0, len(edges_of_random_vertex_1.available_edges) )
        random_vertex_2 = edges_of_random_vertex_1.available_edges[random_index_2]

        # get the parent of the other parent
        #random_vertex_2 = random_vertex_2
        other_parent_vertex = (self.vertices[random_vertex_2]).parent_vertex
        while random_vertex_2 != other_parent_vertex:
            parent_edge = self.vertices[other_parent_vertex]
            other_parent_vertex = parent_edge.parent_vertex
            random_vertex_2 = parent_edge.start_vertex

        edges_of_random_vertex_1.parent_vertex = other_parent_vertex
        edges_of_random_vertex_2 = self.vertices[random_vertex_2]

        #if random_vertex_2 not in self.available_vertices:
        #    print "random_vertex_2 not in self.available_vertices", random_vertex_2, self.available_vertices

        # transfer the contracted vertex to the other
        transfer_vertices = copy.deepcopy(edges_of_random_vertex_1.contracted_vertexs)
        transfer_vertices.append(random_vertex_1)

        if random_vertex_1 == random_vertex_2:
            print "vertex 1 and 2 are the same", random_vertex_1, random_vertex_2
        elif (random_vertex_1 == 0) or (random_vertex_2 == 0):
            print "vertex 1 and/or 2 is zero", random_vertex_1, random_vertex_2

        if debug_mode:
            print "first vertex going into second vertex, along with its contracted vertex list:", random_vertex_1, random_vertex_2, transfer_vertices


        edges_of_random_vertex_2.Contract( edges_of_random_vertex_1, transfer_vertices)

        return True

    def count_crossing_edges(self):
        available_vertex_1 = self.available_vertices[0]
        available_vertex_2 = self.available_vertices[1]

        # this is the first contracted group of vertices
        contracted_vertice_list_1 = (self.vertices[available_vertex_1]).contracted_vertexs
        contracted_vertice_list_1.append(available_vertex_1)

        # this is the second contracted group of vertices
        contracted_vertice_list_2 = (self.vertices[available_vertex_2]).contracted_vertexs
        contracted_vertice_list_2.append(available_vertex_2)
        # These are the list of all the adjacent vertices to the second contracted group of vertices
        edges_of_random_vertex_2 = (self.vertices[available_vertex_2]).edges
        edges_of_random_vertex_2.append(available_vertex_2)

        vertices_on_boundary = []
        # find what vertices are on the boundary
        for vertex in contracted_vertice_list_1:
            if vertex in edges_of_random_vertex_2:
                vertices_on_boundary.append(vertex)

        # for the vertices on bourndary, find which one cross onto the other side
        crossing_edges = 0
        for vertex in vertices_on_boundary:
            for edge in (self.vertices[vertex]).initial_edges:
                if edge in contracted_vertice_list_2:
                    crossing_edges = crossing_edges + 1

        if crossing_edges < 2:
            print "bug, crossing edges = ", crossing_edges

        return crossing_edges



def main():
    pass

if __name__ == '__main__':
    main()
