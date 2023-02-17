class Solution:
    def climbStairs(self, n: int) -> int:
        if n in [0,1]:
            return n
        dp = [0]*(n+2)
        dp[1] = 1
        for i in range(2, n+2):
            dp[i] = dp[i-1]+dp[i-2]
        return dp[n+1]