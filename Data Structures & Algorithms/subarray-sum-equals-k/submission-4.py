class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = {0:1 }
        curr =0
        res = -1 
        for index, num in enumerate(nums):
            curr += num
            diff = curr - k
            
            res += prefix.get(diff,0)
            prefix[curr] = 1 + prefix.get(curr,0)
        return res + 1