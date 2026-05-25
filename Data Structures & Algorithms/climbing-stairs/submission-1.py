class Solution:
    def climbStairs(self, n: int) -> int:
        # dp[i] = ways to go from step i -> n
        dp = [0] * (n + 2)

        dp[n] = 1  # base case
        dp[n-1] = 1
        # build from back
        for i in range(n - 1, -1, -1):
            dp[i] = dp[i + 1] + dp[i + 2]

        return dp[0]