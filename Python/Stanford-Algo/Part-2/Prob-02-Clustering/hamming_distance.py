#-------------------------------------------------------------------------------
# Name:        hamming_distance
# Purpose:
#
# Author:      t.hale
#
# Created:     16/07/2014
# Copyright:   (c) t.hale 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#import gmpy
from heapq import *


def ReadBinaryValues( fileName ):

    print "Name of the file: ", fileName
    firstLine = True
    debugCounter = 0

    popcountHeap = []

    for line in open(fileName):
        if( firstLine ):
            print "Number of Nodes = ", line
            edge = line.split()
            numberOfNodes = int(edge[0])
            firstLine = False
        else:
            debugCounter += 1
            # TODO do I need to trim the whitespaces?
            #edge = line.split()
            # Convert the string into a binary value
            #binary = bytearray([x])

            # Remove all spaces, then convert to a binary (stored as an int)
            stripSpaces = ''.join(line.split())
            binary = int(stripSpaces, 2)
            #print "binary = ", binary

            #TODO find a way to get gmpy working!
            #diff = gmpy.popcount(xor_result)
            slow_popcount = stripSpaces.count("1")
            popcountHeap.append( (slow_popcount, binary))

    print "list size = ", len(popcountHeap)

    heapify(popcountHeap)

    return popcountHeap




def ClusterPreFiltering( popcountHeap ):

    print "Pre-Filtering size = ", len(popcountHeap)
    firstLine = True

    comparisonDictionary = {}
    # Use a list of lists to populate the different groups in

    # (Don't remember why I thought this was important): and make sure that
    # the indices match the ones used for the list of nodes to do the comparisons
    # with!
    initialClusters = {}

    sizeOfHeap = len(popcountHeap)
    for index in range(0, sizeOfHeap):
        nextNode = heappop(popcountHeap)
        binary = nextNode[1]
        targetPopcount = nextNode[0]

        if( firstLine ):
            firstLine = False
            initCompareList = [binary]
            comparisonDictionary[targetPopcount] = initCompareList
            initClusterList = [binary]
            initialClusters[targetPopcount] = initClusterList
        else:
            fitsIntoCurrentCluster = False






            #use a different comparison list for each popcount, and only use the ones that are within a pop count of 2 of targetPopcount





            for k in range(3):      #( max( (targetPopcount - 2), 0), min( (targetPopcount + 2), 24)):
                if fitsIntoCurrentCluster:
                    break

                #start with same pop count then work backwards (can't work forwards because those popcounts haven't been pop off the heap yet)
                if( k == 0):
                    j = targetPopcount
                elif( ( k == 1) and ( targetPopcount >= 1) ):
                    j = targetPopcount - 1
                elif( ( k == 2) and ( targetPopcount >= 2) ):
                    j = targetPopcount - 2
                else:
                    break

                if j in comparisonDictionary:
                    comparisonList = comparisonDictionary[j]

                    for i in range(0, len(comparisonList) ):
                        compareTo = comparisonList[i]
                        xor_result = compareTo ^ binary
                        #TODO find a way to get gmpy working!
                        #diff = gmpy.popcount(xor_result)
                        diff = bin(xor_result).count("1")
                        #print diff
                        if( diff <= 2 ):

this should be put onto the initialClusters for the corresponding binary value it matches up with, not for the targetPopcount.



                            fitsIntoCurrentCluster = True
                            if targetPopcount not in initialClusters:
                                initClusterList = [binary]
                                initialClusters[targetPopcount] = initClusterList
                            else:
                                #(initialClusters[targetPopcount]).append( (targetPopcount,initList) )
                                add_list = (initialClusters[targetPopcount])
                                add_list.append(binary)

                            break

            if( not fitsIntoCurrentCluster ):
                if targetPopcount not in comparisonDictionary:
                    initList = [binary]
                    comparisonDictionary[targetPopcount] = initList
                else:
                    (comparisonDictionary[targetPopcount]).append(binary)

                if targetPopcount not in initialClusters:
                    initClusterList = [binary]
                    initialClusters[targetPopcount] = initClusterList
                else:
                    (initialClusters[targetPopcount]).append(binary)


    print "size = ", len(comparisonDictionary)

    return initialClusters



def main():
    initialClusters = ReadBinaryValues("binary_clustering_big.txt.bak")
    #initialClusters = ReadBinaryValues("test_binary_clustering.txt")

    ClusterPreFiltering(initialClusters)

if __name__ == '__main__':
    main()
