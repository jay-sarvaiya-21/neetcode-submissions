class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l,r = 0,len(nums) - 1
        while l < r:
            if nums[l] + nums[r] > target:
                r-=1
            elif nums[r] + nums[l] < target:
                l+=1
            elif nums[r] + nums[l] == target:
                return [l+1,r+1]
        return False

        