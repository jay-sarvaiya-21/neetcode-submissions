class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map={}
        for i,ele in enumerate(nums):
            if ele in map:
                return [map[ele],i]
            rem=target-ele
            map[rem]=i
            
        

        