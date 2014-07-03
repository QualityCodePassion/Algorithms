#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      t.hale
#
# Created:     02/07/2014
# Copyright:   (c) t.hale 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------


###########################################################################################################
# TODO put the following into the File modules
def Schedule( jobList, questionNum ):

    unscheduledList = []

    # calculate the score for every job
    for job in jobList: #range(0, len(jobList))
        weight = job[0]
        length = job[1]
        if( questionNum == 1):
            score = weight - length
        else:
            score = float( float(weight)/float(length) )

        unscheduledList.append( (score, weight, length) )

    # order the jobs in decreasing order of diffs
    # note, the "sorted" function automatically sorts the "ties" (equal values)
    # in the first element of tuple in the order of the second element of tuple
    sortedScores = sorted(unscheduledList, reverse = True)
    #print "sorted scores =  ", sortedScores


    # compute the sum of weighted completion times of the resulting schedule
    completionTime = 0
    weightedCompletionTime = 0
    for job in sortedScores:
        completionTime += job[2]
        weightedCompletionTime += (completionTime * job[1])


    print "Weighted completion time = ", weightedCompletionTime









def ReadJobsFromFile( fileName, jobList ):

    print "Name of the file: ", fileName
    firstLine = True

    for line in open(fileName):
        if( firstLine ):
            firstLine = False
        else:
            #print line
            jobs = line.split()
            jobList.append( (int(jobs[0]), int(jobs[1]) ) )
            #graphFromFile.InsertEdge(int(edge[0]), int(edge[1]))

    return




def main():
    jobList = []
    #filename = "test_jobs.txt"
    filename = "jobs.txt.bak"
    ReadJobsFromFile(filename, jobList)

    questionNum = 2
    Schedule(jobList, questionNum)

if __name__ == '__main__':
    main()
