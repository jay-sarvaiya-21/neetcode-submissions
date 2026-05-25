class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # Include original index as the second element
        heap = []
        for i, (enqueue, process) in enumerate(tasks):
            heap.append([enqueue, i, process])  # index is second now

        # Sort by enqueue time, then index, then processing time
        heap.sort(key=lambda x: (x[0], x[1], x[2]))

        t = 0
        minHeap, res = [], []
        i = 0

        while i < len(heap) or minHeap:
            # Move time forward if CPU is idle
            if not minHeap and t < heap[i][0]:
                t = heap[i][0]

            # Push all available tasks to minHeap (processingTime, index)
            while i < len(heap) and heap[i][0] <= t:
                enqueue, index, processing = heap[i]
                heapq.heappush(minHeap, (processing, index))
                i += 1

            # Pop the task with smallest processingTime (tie-break by index)
            processing, index = heapq.heappop(minHeap)
            t += processing
            res.append(index)

        return res
