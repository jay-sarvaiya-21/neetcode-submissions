class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        q = deque()
        maxHeap = []
        freqMap = Counter(tasks)
        
        for key,value in freqMap.items():
            heapq.heappush(maxHeap,(-value,key))
        heapq.heapify(maxHeap)
        t = 0
        while q or maxHeap:
            print(q,maxHeap)
            t += 1
            if maxHeap:
                value,key =heapq.heappop(maxHeap)
                value += 1
                print(key,value)
                if value < 0:
                    q.append([t+n,value,key])
            if q and not maxHeap:
                t = q[0][0]
            if q and  t == q[0][0]:
                
                t,value,key =q.popleft()
                heapq.heappush(maxHeap,(value,key))
        return t

        