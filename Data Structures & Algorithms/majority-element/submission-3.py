class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        count = 1
        curr = nums[0]

        for i in range(1,len(nums)):
            if count == 0:
                curr = nums[i]
            if curr == nums[i]:
                count += 1
            else:
                count -= 1
            if count == 0:
                curr = nums[i]
        return curr


        

        