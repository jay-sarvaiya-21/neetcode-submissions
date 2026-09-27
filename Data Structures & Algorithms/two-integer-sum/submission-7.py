class Solution:
    def twoSum(self,nums:List[int],target: int) -> List[int]:

        hmap = {}

        for index,num in enumerate(nums):
            if target - num in hmap:
                return [hmap[target - num],index]
            hmap[num] = index
        
        
