#-------------------------------------------------------------------------------
# Name:        ReadWeightedGraphFromFile
# Purpose:
#
# Author:      t.hale
#
# Created:     03/07/2014
# Copyright:   (c) t.hale 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import sys
sys.path.insert(0, '../../../Lib/Graphs/')
import Graphs





def ReadWeightedGraphFromFile( fileName ):

    print "Name of the file: ", fileName
    firstLine = True

    for line in open(fileName):
        if( firstLine ):
            print line
            edge = line.split()
            numberOfVertices = int(edge[0]) + 1
            graphFromFile = Graphs.Graph(numberOfVertices)
            firstLine = False
        else:
            print line
            edge = line.split()
            graphFromFile.InsertEdge(int(edge[0]), int(edge[1]), False, int(edge[2]) )

    return graphFromFile


def main():
    pass

if __name__ == '__main__':
    main()
