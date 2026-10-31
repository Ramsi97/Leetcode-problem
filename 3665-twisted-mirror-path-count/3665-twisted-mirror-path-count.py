class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        mod = 10**9+7
        n, m = len(grid), len(grid[0])
        dp =[[1]*m for _ in range(n)]
        path = 1
        for i in range(n):
            dp[i][0] = [path, path]
            if grid[i][0]:
                path = 0
        path = 1
        for i in range(m):
            dp[0][i] = [path, path]
            if grid[0][i]:
                path = 0

        for i in range(1, n):
            for j in range(1, m):
                left = dp[i][j-1][0]
                top = dp[i-1][j][1]
                if grid[i][j]:
                    dp[i][j] = [top, left]
                else:
                    dp[i][j] = [left+top, left+top]
        
        return dp[n-1][m-1][0]%mod