import math

# from C:\Users\t.hale\Dropbox\MyDocs\RTCMA\Training\Online Courses\Coursera\Stanford - Algorithms - Design and Analysis - Part 1\03 - Week 01\algo-inversions2_typed.pdf


#def Inversion( input ):
#    # Return the number of inversions
#    return numberOfInversions






def SortAndCount( input, length ):
    print "SortAndCount"

    #hard code the values for now
    count = 42
    SortedList = input

    firstLength = int( math.floor( length/2 ) )
    secondLength = length - firstLength

    if ( (length <= 1) or (firstLength <= 0) or (secondLength <= 0) ):
        return (input, length)

    #recurse on first half of input
    (firstSortedB, firstCount) = SortAndCount( input[0:firstLength], firstLength )
    #recurse on second half of input
    (secondSortedC, secondCount) = SortAndCount( input[(firstLength) : length], secondLength )

    i = 0
    j = 0
    combinedSortedD = [None]*length
    for k in range(0,length):
        if( (j >= len(secondSortedC)) or (i < len(firstSortedCB) ) and (firstSortedCB[i] < secondSortedC[j]) ):
            combinedSortedD[k] = firstSortedCB[i]
            i += 1
        else:
            combinedSortedD[k] = secondSortedC[j]
            j += 1

    return (combinedSortedD, (firstCount+secondCount))


# Open the file and convert to a list of ints
fo = open("DummyTextInput.txt")
print "Name of the file: ", fo.name
lines = fo.readlines()
unsortedList = [ int(lines) for lines in lines ]
fo.close()

sortedList, count = SortAndCount( unsortedList, len(unsortedList) )

print sortedList
print count
