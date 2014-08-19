#-------------------------------------------------------------------------------
# Name:        2sat.py
# Purpose:
#
# Author:      t.hale
#
# Created:     12/08/2014
# Copyright:   (c) t.hale 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import collections


def ReadValues( fileName ):

    print "Name of the file: ", fileName
    firstLine = True
    clauseList = []
    valuePositions = []
    #valueStats = []

    for line in open(fileName):
        if( firstLine ):
            size = int( line )
            print "Size of 2 sat = ", size
            firstLine = False

            #init the valuePositions
            for i in range(0, (size*2 +1) ) :
                temp1 = []
                valuePositions.append( temp1 )

        else:
            edge = line.split()
            value0 = int(edge[0])
            value1 = int(edge[1])
            arrayIndex = len( clauseList )
            clauseList.append( (value0, value1 ) )

            # Populate the "valuePositions" for each value
            # note that the "size" needs to be added, because we can't have negative indexs
            adjustedIndex = value0 + size
            tableList = valuePositions[adjustedIndex]
            tableList.append( (arrayIndex, 0) )

            adjustedIndex = value1 + size
            tableList = valuePositions[adjustedIndex]
            tableList.append( (arrayIndex, 1) )

    return clauseList, valuePositions, size


class BackTrackValues:
    def __init__(self, value, depth, solved_positions, single_postions, backtrackSingleQueueCount ):
        self.solved_positions_list = solved_positions
        self.single_postions_list = single_postions
        self.value = value
        self.depth = depth
        self.backtrackSingleQueueCount = backtrackSingleQueueCount



def two_sat( filename, clauseList, valuePositions, size ):
    # pick the first value of the first clause
    firstClauseValue = clauseList[0][0]

    branchQueue = collections.deque()

    # branch for this value and it's negated value and pop the onto the queue

##    # queue 2 (negate value)
##    adjustedIndex_2 = firstClauseNegatedValue + size
##    value_2_list = valuePositions[adjustedIndex_2]
##    # todo, need to work out what needs to go onto the queue
##    single_list_2 = []

    #backtrackStack.append(( BackTrackValues(firstClauseNegatedValue) )
    depthCounter = 0
    firstClauseNegatedValue = -firstClauseValue
    branchQueue.appendleft( (firstClauseNegatedValue, depthCounter ) )

##    # queue 1 (value as is)
##    adjustedIndex_1 = firstClauseValue + size
##    value_1_list = valuePositions[adjustedIndex_1]
##    # Iterate through this list and mark each position as "single" and say what value is single
##    single_list_1 = []
##    #todo, need to work out what needs to go onto the queue
##    for i in value_1_list:
##        newSinglePosition = i[0]
##        tupleAtThisPosition = clauseList[newSinglePosition]
##        newSingleValue[i[1]]

    branchQueue.appendleft( (firstClauseValue, depthCounter ) )

    backtrackStack = []
    listOfSingles = [int(0)]*len(clauseList)
    singlesQueue = []   #collections.deque()
    listOfSolved =[(False, 0)]*len(clauseList)
    previousDepthCounter = depthCounter
    stackSingleQueueAdjustment = 0
    loopCounter = 0
    finishedFirstHalf = False

    while branchQueue:
        # This is basically a DFS over all the possible branches
        nextBranch = branchQueue.popleft()
        nextBranchValue = nextBranch[0]
        nextBranchDepth = nextBranch[1] + 1

        if (nextBranchDepth == 1) and (loopCounter > 1):
            finishedFirstHalf = True

        loopCounter += 1
        if (loopCounter % 10000) == 1:
            print "loop counter, depth = ", loopCounter, nextBranchDepth, finishedFirstHalf, filename

        # If backtracking is required, then keep popping values of stack until
        # the depth of the stack matches the current depth of the next branch
        while nextBranchDepth < previousDepthCounter :
            #print "Backtracking back to depth ", nextBranchDepth
            backtrackPop = backtrackStack.pop()
            backtrackValue = backtrackPop.value
            popSingleQueueConut = backtrackPop.backtrackSingleQueueCount

            # If the single queuee count is negative, a single value was popped without any being put on by that
            # branch, so the other queue counts on the stack will need to be adjusted by this value when they
            # get popped off the stack
            if popSingleQueueConut < 0:
                stackSingleQueueAdjustment += popSingleQueueConut
            else:
                currentSingleQueueCount = popSingleQueueConut
                popSingleQueueConut += stackSingleQueueAdjustment
                stackSingleQueueAdjustment += currentSingleQueueCount
                if stackSingleQueueAdjustment > 0:
                    stackSingleQueueAdjustment = 0
                if popSingleQueueConut > 0:
                    for popCounter in range(0, popSingleQueueConut):
                        if singlesQueue:
                            singlesQueue.pop()
                        else:
                            print "singlesQueue empty with  count = ", popSingleQueueConut

            previousDepthCounter = backtrackPop.depth
            for position in backtrackPop.single_postions_list:
                listOfSingles[position] = 0
            for position in backtrackPop.solved_positions_list:
                listOfSingles[position] = listOfSolved[position][1]
                listOfSolved[position] = (False, 0)

        previousDepthCounter = nextBranchDepth
        backtrackSolvedList = []
        backtrackSingleList = []
        backtrackSingleQueueCount = 0

        # Check the list of singles of the negated value and break out of this loop if it contains this value
        # because this is a dead end (i.e. this branch isn't solvable
        adjustedNegatedIndex = -nextBranchValue + size
        negatedValuePositions = valuePositions[adjustedNegatedIndex]
        solvable = True
        for position in negatedValuePositions:
            if listOfSingles[position[0]] == -nextBranchValue:
                solvable = False
                break
            elif not listOfSolved[position[0]][0]:
                # The single value will be the value that wasn't this one
                if( position[1] == 0 ):
                    otherClauseValue = 1
                else:
                    otherClauseValue = 0
                singleValue = clauseList[position[0]][otherClauseValue]
                listOfSingles[position[0]] = singleValue
                singlesQueue.append( (position[0], singleValue) )
                backtrackSingleQueueCount += 1
                # note this down on the stack for bracktracking
                backtrackSingleList.append(position[0])

        if not solvable:
            # if not solvable, backrack the things that were just put on above
            for position in backtrackSingleList:
                listOfSingles[position] = 0
            for popCounter in range(0, backtrackSingleQueueCount):
                singlesQueue.pop()
            continue

        adjustedIndex = nextBranchValue + size
        # Get the list of all the positions that this value occurs
        branchValuePositions = valuePositions[adjustedIndex]
        for position in branchValuePositions:
            listOfSolved[position[0]] = (True, listOfSingles[position[0]])
            listOfSingles[position[0]] = 0
            # note this down on the stack for bracktracking
            backtrackSolvedList.append(position[0])

##        if len( listOfSolved ) == len( clauseList ) :
##            print "This has been solved!"
##            return

        singleFound = False
        while singlesQueue:
            popSingleStack = singlesQueue.pop()
            backtrackSingleQueueCount -= 1
            #Make sure that this single hasn't been solved already
            if not listOfSolved[popSingleStack[0]][0]:
                singleFound = True
                break


        backtrackStack.append( BackTrackValues( nextBranchValue, nextBranchDepth, backtrackSolvedList, backtrackSingleList, backtrackSingleQueueCount ) )

        solved_counter = 0

        if singleFound:
            nextSingleToProcess = popSingleStack[1]
        else:
            # if no single available, just get one of the other ones
            for i in range(0, len(clauseList) ):
                if listOfSolved[i][0]:
                    solved_counter += 1
                elif not ( listOfSolved[i][0] and listOfSingles[i] ):
                    nextSingleToProcess = clauseList[i][0]
                    singleFound = True
                    break

        if solved_counter >= len(clauseList) :
            print "This has been solved! Filename was: ", filename
            #while backtrackStack:
            #    print backtrackStack.pop().value
            return

        #nextBranchDepth += 1
        branchQueue.appendleft( (-nextSingleToProcess, nextBranchDepth ) )
        branchQueue.appendleft( (nextSingleToProcess, nextBranchDepth ) )


    print "This is NOT solvable!!! Filename was: ", filename





def main():
    filename = "2sat3.txt"
    #filename = "2sat5_reversed.txt.bak"
    #filename = "2sat1.txt.bak"
    #filename = "2sat_test_2.txt"

    #clauseList, valuePositions, size =  ReadValues("2sat_test_2.txt" )
    #clauseList, valuePositions, size =  ReadValues("2sat1.txt.bak" )
    clauseList, valuePositions, size =  ReadValues( filename )


    two_sat( filename, clauseList, valuePositions, size )

if __name__ == '__main__':
    main()
