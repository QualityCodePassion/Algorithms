#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      t.hale
#
# Created:     09/07/2014
# Copyright:   (c) t.hale 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

SET_SIZE = 200000


from heapq import *



# TODO put this in its own module

def ReadAndHeapifyWeightedEdges( fileName ):

    print "Name of the file: ", fileName
    firstLine = True
    weightedHeap = []

    for line in open(fileName):
        if( firstLine ):
            print "Number of Nodes = ", line
            edge = line.split()
            numberOfNodes = int(edge[0])
            firstLine = False
        else:
            edge = line.split()
            heappush( weightedHeap, ( int(edge[2]), int(edge[0]), int(edge[1]) ) )

    return numberOfNodes, weightedHeap




class set_union:
    def __init__(self, numberOfElements):
        self.p = [0]*SET_SIZE; 		               # parent element
        self.size = [1]*SET_SIZE;                  # number of elements in subtree i
    	self.n = numberOfElements;		           # number of elements in set
        self.numberOfUnions = numberOfElements      # number of uninions in the set

        for i in range(SET_SIZE):
            self.p[i] = i


    def find(self, x):
    	if (self.p[x] == x):
    		return(x);
    	else:
    		return( self.find(self.p[x]) );


    def union_sets(self, s1, s2):
    	r1 = self.find(s1);
    	r2 = self.find(s2);

    	if(r1 == r2):
            return;		# already in same set

        # When I do a merge, decrease the "numberOfUnions"
        self.numberOfUnions -= 1

    	if (self.size[r1] >= self.size[r2]):
    		self.size[r1] = self.size[r1] + self.size[r2];
    		self.p[ r2 ] = r1;
    	else:
            self.size[r2] = self.size[r1] + self.size[r2];
            self.p[r1] = r2;


    def same_component(self, s1, s2):
    	return ( find(s1) == find(s2) );




def clustering( numberOfNodes, heapEdges ):
    # Put all the edges onto a heap and repeatedly pop the minmum

    unionCount = 0
    maxDistance = 0
    nodeUninion = set_union(numberOfNodes)
    # Repeat until only 4 clusters left
    while( unionCount != 4 ):
        nextEdge = heappop( heapEdges)
        nodeUninion.union_sets(nextEdge[1], nextEdge[2])
        unionCount = nodeUninion.numberOfUnions
        # The last edge pulled of the heap should be the maximum distance, because
        # we are repeatedly pulling from a heap.
        maxDistance = nextEdge[0]

    return maxDistance




def main():

    #heapEdges = ReadAndHeapifyWeightedEdges("test_clustering1.txt")
    numberOfNodes, heapEdges = ReadAndHeapifyWeightedEdges("clustering1.txt.bak")
    maxDistance = clustering(numberOfNodes, heapEdges)
    print "maxDistance = ", maxDistance

if __name__ == '__main__':
    main()
