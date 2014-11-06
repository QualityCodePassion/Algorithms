#-------------------------------------------------------------------------------
# Name:        module1
#
# Purpose: Solves the knapsack problem
# The "optimized_knapsack_02.py" algorithm found the correct answer by
# filtering out all of the nodes that have a value to weight ratio less than
# 0.5. I obtained this value by analysing and manually inspecting the values
# being used for the computation. This will only work for this dataset, but
# could probably be automated if needed for future datasets.
#
# Author:      t.hale
#
# Created:     19/07/2014
# Copyright:   (c) t.hale 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from operator import itemgetter, attrgetter

max_weight = 0
max_total_value = 0


def ReadValuesAndRatios( fileName ):

    global max_weight

    print "Name of the file: ", fileName
    firstLine = True
    elements = []

    for line in open(fileName):
        if( firstLine ):
            print "Max weight and size = ", line
            edge = line.split()
            maxWeight = int(edge[0])
            max_weight = maxWeight
            numberOfValues = int(edge[1])
            #elements.append( (0,0,0) )    # First element should start at 1
            firstLine = False
        else:
            edge = line.split()
            value = int(edge[0])
            weight = int(edge[1])
            value_ratio = float( float(value)/float(weight) )
            #value_ratio = value/weight
            elements.append( (value_ratio, weight, value) )

    # TOTO sort by descending the ratio fist, but then ascending then weight.
    #elements.sort( reverse=True )
    #sorted( elements, key=itemgetter(2) )
    #sorted( elements, key=itemgetter(1)  )
    #sorted( elements, key=itemgetter(0), reverse=True )
    #elements.sort(key=lambda x: (order.index(x[0]), x[2], x[3]))

    elements.sort(key=lambda k: (k[0], -k[1]), reverse=True)

    return maxWeight, numberOfValues, elements


def DFS( sorted_ratio, solution_trace, current_ratio_head, current_solution_head, recursion_depth ):

    global max_total_value
    global max_weight

    #explored[current_solution_head] = True
    current_total_weight, current_value_total = solution_trace[current_solution_head]
    recursion_depth += 1

    for i in range(current_ratio_head, len(sorted_ratio) ):
        nextNode = sorted_ratio[i]
        next_weight = nextNode[1]
        next_ratio = nextNode[0]
        if( next_ratio < 0.5 ):
            break

        if current_total_weight + next_weight <= max_weight:
            current_solution_head += 1
            next_value = nextNode[2]
            next_value += current_value_total
            next_weight += current_total_weight
            if next_value > max_total_value:
                max_total_value = next_value
                print "recursion_depth, new max value = ", recursion_depth, max_total_value
            solution_trace[current_solution_head] = next_weight, next_value
            DFS( sorted_ratio, solution_trace, (i+1), current_solution_head, recursion_depth)

    #print "current_ratio_head, max value = ", current_ratio_head, max_total_value
    recursion_depth -= 1


        # flag that this node has been explored


def main():
    maxWeight, numberOfValues, sorted_ratio = ReadValuesAndRatios("knapsack_big.txt.bak")
    #maxWeight, numberOfValues, sorted_ratio = ReadValuesAndRatios("knapsack1.txt")
    #maxWeight, numberOfValues, sorted_ratio = ReadValuesAndRatios("test_knapsack_2.txt")

    current_tace = [(0,0)]*( len(sorted_ratio) + 1 )

    recursion_depth = 0
    DFS( sorted_ratio, current_tace, 0, 0, recursion_depth )



    print "Max value = ", max_total_value

if __name__ == '__main__':
    main()
