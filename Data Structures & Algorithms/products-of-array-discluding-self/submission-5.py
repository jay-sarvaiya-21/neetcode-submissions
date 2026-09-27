class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        N = len(nums)
        prod = 1
        left, right = [1]* N, [1]* N

       
        for i in range(len(nums)):
            left[i] = prod
            prod = prod * nums[i]
        prod = 1
        for i in range(len(nums)-1 ,-1,-1):
            right[i] = prod
            prod*= nums[i]
        res = [left[i] * right[i] for i in range(len(left))]

        return res




        

