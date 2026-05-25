class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        #6.46

        dp = [1 for _ in range(len(nums))]

        for i in range(len(nums)-2,-1,-1):
            for j in range(i,len(nums)):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i],1 + dp[j])
        return max(dp)

        