class Solution:

    
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        
        n = len(nums)
        left = [1 for _ in range(n)]
        right = [1 for _ in range(n)]
        l, r = 1, 1

        for i in range(1,n):
            left[i] = l * nums[i-1]
            l *= nums[i-1]

        for i in range(n-2,-1,-1):
            right[i] = r * nums[i+1]
            print(r,right[i])
            r *= nums[i+1]
            
        
        # [ 1 1 2 8]
        # [48  24  6 1]
        print(left)
        print(right)
  
        return [left[i] * right[i] for i in range(n)]
        