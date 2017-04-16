__author__ = 'thale'

import random
import math
import copy

# To import the graph module, you deed to add the following path to import the lib from a different directory
#import sys
#sys.path.insert(0, '../../../Lib/Graphs/')
#import Graphs


###########################################################################################################
# ReadSumsFromFile

debug_mode = True

def ReadSumsFromFile( fileName ):

    print "Name of the file: ", fileName
    integer_dict = {}

    for line in open(fileName):
        #print line

        next_int = int( line )
        integer_dict[next_int] = next_int

        #print integer_dict

    return integer_dict


# End of file stuff
###########################################################################################################


###########################################################################################################
# 2 sum
def two_sum(integer_dict):
    num_of_sums = 0

    for t in range(-10000,10001):

        #if (t == -10000) or (t == 10000):
        print t

        #previous_sum_values = {}

        for x in integer_dict:
            y = t - x
            if ( x != y) and ( y in integer_dict): # and ( y not in previous_sum_values) and ( x not in previous_sum_values):
                print "x + y = t", x,y,t
                num_of_sums = num_of_sums + 1
                #previous_sum_values[x] = x
                #previous_sum_values[y] = y

                break

    print "total number of 2 sums = ", num_of_sums

    return num_of_sums



# End of 2 sum
###########################################################################################################


def main():
    #filename = "test_data_2sum.txt"
    filename = "algo1_programming_prob_2sum.txt"

    integer_dict = ReadSumsFromFile( filename )
    two_sum( integer_dict)



if __name__ == '__main__':
    main()