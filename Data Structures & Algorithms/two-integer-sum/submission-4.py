class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hashmap = {}

        for indx,ele in enumerate(nums):
            diff = target - ele
            if diff in hashmap:
                return [hashmap[diff],indx]
            hashmap[ele] = indx

        