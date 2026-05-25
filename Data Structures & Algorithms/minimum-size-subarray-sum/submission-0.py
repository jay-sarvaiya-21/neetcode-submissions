class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        curr = 0
        if sum(nums) < target:
            return 0
        l,r = 0,0
        res = float("infinity")
        for r,num in enumerate(nums):
            curr += num
            while curr - nums[l] >= target:
                curr -= nums[l]
                l += 1
            if curr >= target:
                res = min(res, r - l +1)
        return res

        