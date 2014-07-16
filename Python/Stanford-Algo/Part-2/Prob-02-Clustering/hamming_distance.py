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

def ReadBinaryValues( fileName ):

    print "Name of the file: ", fileName
    firstLine = True

    # Use a list of lists to populate the different groups in and make sure that
    # the indices match the ones used for the list of nodes to do the comparisons
    # with!
    comparisonList = []
    initialClusters = []

    for line in open(fileName):
        if( firstLine ):
            print "Number of Nodes = ", line
            edge = line.split()
            numberOfNodes = int(edge[0])
            firstLine = False
        else:
            # TODO do I need to trim the whitespaces?
            #edge = line.split()
            # Convert the string into a binary value
            #binary = bytearray([x])

            # Remove all spaces, then convert to a binary (stored as an int)
            stripSpaces = ''.join(line.split())
            binary = int(stripSpaces, 2)
            #print "binary = ", binary

            if( not comparisonList ):
                comparisonList.append(binary)
                initList = [binary]
                initialClusters.append(initList)
            else:
                fitsIntoCurrentCluster = False
                for i in range(0, len(comparisonList)):
                    compareTo = comparisonList[i]
                    xor_result = compareTo ^ binary
                    #TODO find a way to get gmpy working!
                    #diff = gmpy.popcount(xor_result)
                    diff = bin(xor_result).count("1")
                    #print diff
                    if( diff <= 2 ):
                        initialClusters[i].append(binary)
                        fitsIntoCurrentCluster = True
                        break

                if( not fitsIntoCurrentCluster ):
                    comparisonList.append(binary)
                    initList = [binary]
                    initialClusters.append(initList)



    print "size = ", len(comparisonList)

    return initialClusters


def main():
    #initialClusters = ReadBinaryValues("test_binary_clustering.txt")
    initialClusters = ReadBinaryValues("binary_clustering_big.txt.bak")

if __name__ == '__main__':
    main()
