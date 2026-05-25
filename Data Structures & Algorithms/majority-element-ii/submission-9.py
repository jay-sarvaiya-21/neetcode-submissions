class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        hmap = {}

        for num in nums:
            hmap[num] = 1 + hmap.get(num,0)
            if len(hmap) <= 2:
                continue
            newMap = {}
            for keys in hmap:

                newMap[keys]= hmap[keys] - 1
                if newMap[keys] == 0:
                    del newMap[keys]
            hmap = newMap

        res = []
        for keys in hmap:
            if nums.count(keys) > len(nums)/ 3:
                res.append(keys)
        return res          