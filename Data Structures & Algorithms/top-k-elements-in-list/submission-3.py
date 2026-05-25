class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # 0 1 2 3 4 5 6 7
        bucket = [[] for i in range(len(nums)+ 1)] 
        hashMap = {}
        res = []

        for num in nums:
            hashMap[num] = 1 + hashMap.get(num,0)
        print(hashMap)
        print(bucket)
        for key,value in hashMap.items():
            print(value)
            bucket[value].append(key)
            print(bucket)
        
        for i in range(len(bucket)-1,-1,-1):
            for val in bucket[i]:
                res.append(val)
                if len(res) == k:
                    return res




        

        
        