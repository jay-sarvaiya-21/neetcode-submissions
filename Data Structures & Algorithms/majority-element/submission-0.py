class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = {}
        for num in nums:
            hashmap[num] = hashmap.get(num,0) + 1
        for key,value in hashmap.items():
            if value >= len(nums)//2 :
                return key