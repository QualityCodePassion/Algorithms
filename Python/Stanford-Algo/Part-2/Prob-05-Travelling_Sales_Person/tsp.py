#-------------------------------------------------------------------------------
# Name:        tsp.py
# Purpose:     Solves the travelling sales person problem using dynamic programming
#
# Author:      t.hale
#
# Created:     31/07/2014
# Copyright:   (c) t.hale 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import itertools
import math


def testCombinations():
    testList = ["1", "2", "10", "30", "100"]
    print testList

    testDict = {}

    for i in (itertools.combinations(testList, 3)):
        testDict[i] = range(5)

    testDict[("1","2")] = 12
    testDict[("1","2","3","4")] = 12

    print (testDict[("1","2","10")])[3]



def read_tsp_cities( file_name ):
    print "Name of the file: ", file_name
    firstLine = True
    list_of_cities = []

    for line in open(file_name):
        if( firstLine ):
            print line
            line_data = line.split()
            numberOfCites = int(line_data[0])
            firstLine = False
        else:
            line_data = line.split()
            list_of_cities.append( (float(line_data[0]), float(line_data[1]) ) )

    return list_of_cities


def calc_distance( city_1, city_2 ):
    return math.sqrt( math.pow( (city_1[0] - city_2[0]), 2) + math.pow( (city_1[1] - city_2[1]), 2) )



def tsp( list_of_cities ):
    number_of_cities = len(list_of_cities)
    initList = [float("inf")]*( number_of_cities )
    initList[0] = 0
    A = {}
    A[("0",)] = initList
    full_set_without_0 = []

    # init the full set
    for i in range(1, number_of_cities):
        full_set_without_0.append(str(i) )

    # for each subproblem size 2,3,...,number_of_cities
    for m in range(1, (number_of_cities) ):
        # for each combination of  the full set of size m
        # note that "0" has to be in every subset
        for S_tuple in (itertools.combinations(full_set_without_0, m)):
            S = ["0"]
            S += (S_tuple)
            # for each j in this subset S (that isn't "0")
            for j_str in S:
                if( j_str != "0" ):
                    j = int(j_str)
                    s_without_j = list(S)
                    s_without_j.remove(j_str)
                    key = tuple(s_without_j)
                    subset = A[key]
                    min_value = float("inf")
                    for k in range(len(subset) ):
                        if( k != j):
                            C_kj = calc_distance( list_of_cities[k], list_of_cities[j] )
                            new_contender = subset[k] + C_kj
                            if( new_contender < min_value ):
                                min_value = new_contender
                    tuple_key = tuple(S)
                    if tuple_key not in A:
                        A[tuple_key] = [float("inf")]*( number_of_cities )

                    A[tuple_key][j] = min_value

                    #if list_for_s.count
                    # if j_str in S: S.remove(j_str)

    full_set = tuple( ["0"] + full_set_without_0 )
    subset = A[full_set]
    min_value = float("inf")
    for j in range(1, number_of_cities):
        C_j0 = calc_distance( list_of_cities[j], list_of_cities[0] )
        new_contender = subset[j] + C_j0
        if( new_contender < min_value ):
            min_value = new_contender

    return int( min_value )




def main():
    #testCombinations()
    #list_of_cities = read_tsp_cities("test_tsp_01.txt")
    list_of_cities = read_tsp_cities("tsp.txt")
    min_value = tsp(list_of_cities)
    print "min cost = ", min_value

if __name__ == '__main__':
    main()
