class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
       count = {}
       heap = []
       res = []
       for num in nums:
        count[num] = 1 + count.get(num,0)
       for val,freq in count.items():
        heap.append((-freq,val))
       heapq.heapify(heap)
       for i in range(k):
        res.append(heapq.heappop(heap)[-1])
       return res       
    

        