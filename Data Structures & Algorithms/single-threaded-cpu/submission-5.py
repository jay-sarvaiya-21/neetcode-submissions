import heapq
from typing import List

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # add original index
        tasks = [(et, pt, i) for i, (et, pt) in enumerate(tasks)]
        tasks.sort()  # sort by enqueueTime

        res = []
        minHeap = []
        time = 0
        i = 0
        n = len(tasks)

        while i < n or minHeap:
            # If CPU idle, jump to next task
            if not minHeap and time < tasks[i][0]:
                time = tasks[i][0]

            # push all tasks that have arrived by current time
            while i < n and tasks[i][0] <= time:
                enqueueTime, processingTime, index = tasks[i]
                heapq.heappush(minHeap, (processingTime, index))
                i += 1

            # pick next task
            processingTime, index = heapq.heappop(minHeap)
            time += processingTime
            res.append(index)

        return res


            

        