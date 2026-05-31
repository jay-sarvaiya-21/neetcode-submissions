class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, r = 0, len(nums) - 1
        i = 0

        while i < (len(nums)):
            
            if nums[i] == 0 and l <= i:
                nums[l], nums[i] = nums[i], nums[l]
                l += 1
                i -= 1
            elif nums[i] == 2 and r >= i:
                nums[r], nums[i] = nums[i], nums[r]
                r -= 1
                i -= 1
            i += 1
            
                

          