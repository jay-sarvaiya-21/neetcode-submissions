class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 1
        key = nums[0]
        for i in range(1,len(nums)):
            if key == nums[i]:
                count += 1
            else:
                count -= 1
            if count == 0:
                key = nums[i]
                count = 1
        return key

            

