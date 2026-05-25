class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = [-num for num in nums]
        heapq.heapify(maxHeap)
        for i in range(k):
            x = -heapq.heappop(maxHeap)
        return x
        