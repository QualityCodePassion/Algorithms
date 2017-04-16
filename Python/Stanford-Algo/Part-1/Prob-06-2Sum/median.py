__author__ = 'thale'

from heapq import *
import sys

# To import the graph module, you deed to add the following path to import the lib from a different directory
#import sys
#sys.path.insert(0, '../../../Lib/Graphs/')
#import Graphs


###########################################################################################################
# ReadAndCalcMedianSum

debug_mode = False

def ReadAndCalcMedianSum( fileName ):

    print "Name of the file: ", fileName
    min_heap = []   # This stores all the largest values, so that the min one could be the median
    max_heap = []   # This stores all of the smallest values, so that the max could be the median

    median_sum = 0

    for line in open(fileName):
        if debug_mode:
            print line

        next_int = int( line )

        if not max_heap:
            heappush( max_heap, -next_int )
        elif next_int <= -max_heap[0]:  #max_heap_max_value:
            inserted_into_min_heap = False
            # makes sure to keep the two heaps balanced, so move one to other when one gets bigger
            if len(max_heap) > len(min_heap):
                if next_int > -max_heap[0]:
                    heappush( min_heap, next_int )
                    inserted_into_min_heap = True
                else:
                    temp = heappop( max_heap )
                    temp = (-1)*temp
                    if min_heap and (temp > min_heap[0]):
                        print "Min: this shouldn't happen and could be caused by a bug!", min_heap[0], temp

                    heappush( min_heap, temp)

            if not inserted_into_min_heap:
                heappush( max_heap, -next_int )

        elif not min_heap:
            heappush( min_heap, next_int )
        else:
            inserted_into_max_heap = False
            # makes sure to keep the two heaps balanced, so move one to other when one gets bigger
            if len(max_heap) < len(min_heap):
                if min_heap and ( next_int < min_heap[0] ):
                    heappush( max_heap, -next_int )
                    inserted_into_max_heap = True
                else:
                    temp = heappop( min_heap )
                    if temp < -max_heap[0]:
                        print "min heap size, max heap size", len(min_heap), len(max_heap)
                        print "Max: this shouldn't happen and could be caused by a bug!", -max_heap[0], temp

                    heappush( max_heap, -temp)

            if not inserted_into_max_heap:
                heappush( min_heap, next_int )


        #min_heap_min_value = min_heap[0]
        #max_heap_max_value = -max_heap[0]

        if len(max_heap) > (1 + len(min_heap) ) :
            raise "max heap is more than 1 bigger than min heap", len(max_heap), len(min_heap)
        elif len(min_heap) > (1 + len(max_heap) ) :
            raise "min heap is more than 1 bigger than max heap", len(min_heap), len(max_heap)

        if len(max_heap) >= len(min_heap):
            median_sum = median_sum -max_heap[0]
            if debug_mode:
                print "median = ", -max_heap[0]
        else:
            median_sum = median_sum + min_heap[0]
            if debug_mode:
                print "median = ", min_heap[0]

    return_value = median_sum % 10000
    print "Last 4 didgits of sum of median = ", return_value


    return return_value


# End
###########################################################################################################




def main():
    #filename = "test_median_data.txt"
    filename = "Median.txt"

    integer_dict = ReadAndCalcMedianSum( filename )



if __name__ == '__main__':
    main()