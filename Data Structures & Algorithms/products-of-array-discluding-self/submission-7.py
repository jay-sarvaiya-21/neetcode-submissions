class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        N = len(nums)
        prod = [1] * N
        left, right = [1]* N, [1]* N
        temp = 1
       
        for i in range(len(nums)):
            prod[i] = temp
            temp = temp * nums[i]
        temp = 1
      
        for i in range(len(nums)-1 ,-1,-1):
            prod[i]*= temp
            temp*=  nums[i]
        return prod




        

