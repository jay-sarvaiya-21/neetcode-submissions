class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        curr_sum = 0
        res = min(nums)

        for num in nums:
            curr_sum += num
            print(curr_sum)
            res = max(curr_sum,res)
            if curr_sum < 0:
                curr_sum = 0
            

        return res
        