class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:


        maxHeap = []

        count = {}

        for num in nums:
            count[num] = 1 + count.get(num,0)
            
        for key,value in count.items():
            heapq.heappush(maxHeap,(-value,key))
        res = []
        for i in range(k):
            value,key =heapq.heappop(maxHeap)
            res.append(key)
        return res

        
        