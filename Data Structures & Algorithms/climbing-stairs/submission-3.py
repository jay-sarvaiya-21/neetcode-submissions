class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        next1 = 1  # dp[n-1]
        next2 = 1  # dp[n]

        for i in range(n - 2, -1, -1):
            curr = next1 + next2   # dp[i]
            next2 = next1          # shift
            next1 = curr

        return next1