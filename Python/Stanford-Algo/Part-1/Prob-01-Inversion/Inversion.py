import math
# Need to add the following path to import the lib from a different directory
import sys
sys.path.insert(0, '../Lib/FileIO/')
import FileArray

# from C:\Users\t.hale\Dropbox\MyDocs\RTCMA\Training\Online Courses\Coursera\Stanford - Algorithms - Design and Analysis - Part 1\03 - Week 01\algo-inversions2_typed.pdf


def SortAndCount( input, length ):
    #print "SortAndCount"

    firstLength = int( math.floor( length/2 ) )
    secondLength = length - firstLength

    if ( (length <= 1) or (firstLength <= 0) or (secondLength <= 0) ):
        return (input, 0)

    #recurse on first half of input
    (firstSortedB, firstCount) = SortAndCount( input[0:firstLength], firstLength )
    #recurse on second half of input
    (secondSortedC, secondCount) = SortAndCount( input[(firstLength) : length], secondLength )

    # Merge and count
    i = 0
    j = 0
    combinedSortedD = [None]*length
    combinedCountD = firstCount+secondCount;
    for k in range(0,length):
        if( (j >= len(secondSortedC)) or (i < len(firstSortedB) ) and (firstSortedB[i] < secondSortedC[j]) ):
            combinedSortedD[k] = firstSortedB[i]
            i += 1
        else:
            combinedSortedD[k] = secondSortedC[j]
            j += 1
            # counting is explained on page 8 of "algo-inversions2_typed.pdf" mentioned above.
            # Each time an elememnt of the "second array C" is merged, increment the count
            # by the namber of remaining elements in the "first array B"
            combinedCountD += (len(firstSortedB) - i)

    return (combinedSortedD, combinedCountD)


# Open the file and convert to a list of ints
#unsortedList = FileArray.FileIntegerArray("IntegerArray.txt.bak")
unsortedList = FileArray.FileIntegerArray("TestIntegerArray.txt.bak")

sortedList, count = SortAndCount( unsortedList, len(unsortedList) )

#print sortedList
print "Count Value is = "
print count
