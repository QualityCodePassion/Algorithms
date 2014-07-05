#-------------------------------------------------------------------------------
# Name:         PriorityQueue
# Purpose:      Heap implementation of a Priority queue taken from
#               https://docs.python.org/2/library/heapq.html
#               Allows a key to be "removed"
#
# Author:      t.hale
#
# Created:     03/07/2014
#-------------------------------------------------------------------------------

import sys
import itertools
from heapq import *

REMOVED = '<removed-task>'      # placeholder for a removed task


class PriorityQueue:
    def __init__(self):
        self.pq = []                         # list of entries arranged in a heap
        self.entry_finder = {}               # mapping of tasks to entries
        self.counter = itertools.count()     # unique sequence count

    def add_task(self, task, priority=0):
        'Add a new task or update the priority of an existing task'
        if task in self.entry_finder:
            self.remove_task(task)
        count = next(self.counter)
        entry = [priority, count, task]
        self.entry_finder[task] = entry
        heappush(self.pq, entry)

    def remove_task(self, task):
        'Mark an existing task as REMOVED.  Raise KeyError if not found.'
        entry = self.entry_finder.pop(task)
        entry[-1] = REMOVED

    def pop_task(self):
        'Remove and return the lowest priority task, prioirty value and a flag to signal if empty.'
        while self.pq:
            priority, count, task = heappop(self.pq)
            if task is not REMOVED:
                del self.entry_finder[task]
                return task, priority, False

        task = sys.maxint
        priority = sys.maxint
        return task, priority, True

def main():
    heapQueue = PriorityQueue()
    heapQueue.add_task(9,9)
    heapQueue.add_task(4,4)
    heapQueue.add_task(45,45)
    heapQueue.add_task(88,88)
    heapQueue.add_task(2,2)
    heapQueue.add_task(69,1)
    heapQueue.add_task(50,50)
    heapQueue.add_task(77,77)
    heapQueue.add_task(42,42)

    heapQueue.remove_task(88)
    heapQueue.remove_task(50)

    heapQueue.add_task(50,50)

    while(True):
        print heapQueue.pop_task()

if __name__ == '__main__':
    main()
