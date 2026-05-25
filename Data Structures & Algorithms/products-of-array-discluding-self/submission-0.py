class Solution:

    def rev(self,arr):
        l = 0 
        r = len(arr) - 1
        while l < r:
            arr[l],arr[r] = arr[r],arr[l]
            l+= 1
            r-= 1
        return arr
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        left = [1] * len(nums)
        right = [1] * len(nums)
        l,r = 1,1

        for i,num in enumerate(nums):
            left[i]*= l
            l*= num
        rev = self.rev(nums)
        for i,num in enumerate(rev):
            right[i]*= r
            r*= num
        right = self.rev(right)
        return [left[i] * right[i] for i in range(len(left))]
        