class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        n, m = len(matrix), len(matrix[0])
        result = 0
        direction = [(1, 0), (0, 1), (0, -1), (-1, 0)]
        grid = [[0]*m for _ in range(n)]

        def inbound(row, col):
            return 0 <= row < n and 0 <= col < m

        def dfs(row, col):
            if grid[row][col] != 0:
                return grid[row][col]
            result = 0
            for a, b in direction:
                new_row, new_col = row+a, col+b
                if inbound(new_row, new_col) and matrix[row][col] < matrix[new_row][new_col]:
                    result = max(result, dfs(new_row, new_col))
            grid[row][col] = result+1
            return result+1

        ans = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    grid[i][j] = dfs(i, j)
                    ans = max(ans, grid[i][j])
        return ans