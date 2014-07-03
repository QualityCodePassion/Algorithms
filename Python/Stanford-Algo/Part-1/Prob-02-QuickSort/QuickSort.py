import math
# Need to add the following path to import the lib from a different directory
import sys
sys.path.insert(0, '../Lib/FileIO/')
import FileArray

# From C:\Users\t.hale\Dropbox\MyDocs\RTCMA\Training\Online Courses\Coursera\Stanford - Algorithms - Design and Analysis - Part 1\05 - Week 02\5-2-algo-qsort-partition-annotated.pdf (page 8)


runningcomparisoncount = 0
pivotType =3

def swap( inArray, pos1, pos2):
    temp1 = inArray[pos1]
    temp2 = inArray[pos2]
    inArray[pos2] = temp1
    inArray[pos1] = temp2


def GetPivot( inArray, start, end ):
    if( pivotType == 1 ):
        # Use the first element for the first part of question
        return inArray[start], start
    elif( pivotType == 2 ):
        # Use the second element for the second part of question
        return inArray[end], end
    else:
        #Use the "median of three" for the third part of question
        middleElement = start + int( math.floor( (end-start)/2 ) )
        middleValue = inArray[middleElement]
        firstValue = inArray[start]
        lastValue = inArray[end]

        # return the median of these three values
        if( ( (middleValue >= firstValue) and (middleValue <= lastValue) )
        or ( (middleValue <= firstValue) and (middleValue >= lastValue) ) ):
            return middleValue, middleElement


        if( ( (firstValue >= middleValue) and (firstValue <= lastValue) )
        or ( (firstValue <= middleValue) and (firstValue >= lastValue) ) ):
            return firstValue, start

        if( ( (lastValue >= middleValue) and (lastValue <= firstValue) )
        or ( (lastValue <= middleValue) and (lastValue >= firstValue) ) ):
            return lastValue, end

        raise(RuntimeError, "No middle value found")


def partition( inArray, start, end ):
    if( (end <= 0) or (end <= start) ):
        return

    (pivotValue, pivotPos) = GetPivot( inArray, start, end )
    #put the pivot at the start for partitioning
    swap(inArray, start, pivotPos)

    # do the partitioning with pivot at start
    i = start + 1
    for j in range( (start+1), (end+1) ):
        global runningcomparisoncount
        runningcomparisoncount += 1
        if( inArray[j] < pivotValue ):
            #swap inArray[j] and inArray[i]
            swap(inArray, j, i)
            i += 1

    #swap pivot element and inArray[i-1]
    swap(inArray, start, (i-1) )

    #Then recursively sort 1st part
    partition(inArray, start, i-2)

    #Then recursively sort 2nd part
    partition(inArray, i, end)


def main():
    # Open the file and convert to a list of ints
    debug = False
    if( debug ):
        unsortedList = FileArray.FileIntegerArray("../Data/DummyTextInput.txt")
    else:
        unsortedList = FileArray.FileIntegerArray("C:/Users/t.hale/Dropbox/dev/GitHub/Datasets/Algorithms/QuickSort.txt")

    partition(unsortedList, 0, (len(unsortedList)-1) )
    print "Count = ", runningcomparisoncount

    if( debug ):
        print "Sorted array = "
        print unsortedList


if __name__ == '__main__':
    main()
