import math
# Need to add the following path to import the lib from a different directory
import sys
sys.path.insert(0, '../Lib/FileIO/')
import FileArray

# From C:\Users\t.hale\Dropbox\MyDocs\RTCMA\Training\Online Courses\Coursera\Stanford - Algorithms - Design and Analysis - Part 1\05 - Week 02\5-2-algo-qsort-partition-annotated.pdf (page 8)

def swap( inArray, pos1, pos2):
    temp1 = inArray[pos1]
    temp2 = inArray[pos2]
    inArray[pos2] = temp1
    inArray[pos1] = temp2


def partition( inArray, start, end ):
    if( (end <= 0) or (end <= start) ):
        return

    pivot = inArray[start]
    i = start + 1
    for j in range( (start+1), (end+1) ):
        if( inArray[j] < pivot ):
            #swap inArray[j] and inArray[i]
            swap(inArray, j, i)
            i += 1

    #swap inArray[start] and inArray[i-1]
    swap(inArray, start, (i-1) )

    #Then recursively sort 1st part
    partition(inArray, start, i-2)

    #Then recursively sort 2nd part
    partition(inArray, i, end)


# Open the file and convert to a list of ints
unsortedList = FileArray.FileIntegerArray("../Data/DummyTextInput.txt")
partition(unsortedList, 0, (len(unsortedList)-1) )
print "Sorted array = "
print unsortedList


