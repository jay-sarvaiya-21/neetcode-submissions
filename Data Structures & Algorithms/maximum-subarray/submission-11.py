class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        currSum = 0
        res = nums[0]
        for r in range(len(nums)):
            currSum += nums[r] 
            res = max(currSum,res)
            if currSum < 0:
                currSum = 0
        return res


        
        