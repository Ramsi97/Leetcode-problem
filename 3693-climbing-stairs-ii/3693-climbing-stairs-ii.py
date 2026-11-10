class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        

        dp = [float("inf")]*(n+1)
        dp[0] = 0

        for i in range(n):
            for j in range(1, min(i+2, 4)):
                dp[i+1] = min(dp[i+1], costs[i] + dp[i+1-j]+ (j)**2)
        return dp[n]