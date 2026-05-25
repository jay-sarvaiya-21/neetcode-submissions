class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        bucket = {index: [] for index in range(len(nums)+1)}
        freq = Counter(nums)
        for value, freq in freq.items():
            bucket[freq].append(value)
        
        for i in range(len(nums),0,-1):
            for num in bucket[i]:

                res.append(num)
                if len(res) == k:
                    return res

        
        