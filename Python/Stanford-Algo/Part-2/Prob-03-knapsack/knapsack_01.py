#-------------------------------------------------------------------------------
# Name:        knapsack_01.py
# Purpose:
#
# Author:      t.hale
#
# Created:     18/07/2014
# Copyright:   (c) t.hale 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def ReadValuesAndWeights( fileName ):

    print "Name of the file: ", fileName
    firstLine = True
    elements = []

    for line in open(fileName):
        if( firstLine ):
            print "Max weight and size = ", line
            edge = line.split()
            maxWeight = int(edge[0])
            numberOfValues = int(edge[1])
            elements.append( (0,0) )    # First element should start at 1
            firstLine = False
        else:
            edge = line.split()
            elements.append( (int(edge[0]), int(edge[1]) ) )

    return maxWeight, numberOfValues, elements


def CalculateKnapsack( maxWeight, numberOfValues, elements ):

    # initialize the 2-D array with a list of lists
    A = []
    for i in range(numberOfValues + 1):
        column = [0]*(maxWeight + 1)
        A.append(column)

    print A[numberOfValues][maxWeight]

    for i in range(1, numberOfValues+1):
        for x in range(maxWeight+1):
            value_i, weight_i = elements[i]
            x_minus_weight_i = x - weight_i
            if(x_minus_weight_i < 0 ):
                x_minus_weight_i = 0

            A[i][x] = max( (A[i - 1][x]), (A[i - 1][x_minus_weight_i] + value_i) )

    return A[numberOfValues][maxWeight]



##            rows = (matrix[i])
##            column = row[x]
##            column = i + x






def main():
    maxWeight, numberOfValues, elements = ReadValuesAndWeights("test_knapsack_2.txt")
    #maxWeight, numberOfValues, elements = ReadValuesAndWeights("knapsack1.txt")

    optimalSol = CalculateKnapsack(maxWeight, numberOfValues, elements)
    print "optimalSol = ", optimalSol

if __name__ == '__main__':
    main()
