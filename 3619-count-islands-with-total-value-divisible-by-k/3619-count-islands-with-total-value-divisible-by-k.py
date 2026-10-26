class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        rows, cols = len(grid), len(grid[0])

        def inbound(row, col):
            return 0<=row < rows and 0 <= col < cols
        dirn = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        def dfs(row, col):
            result = grid[row][col]
            grid[row][col] = 0

            for dx, dy in dirn:
                if inbound(row+dx, col+dy) and grid[row+dx][col+dy]:
                    result += dfs(row+dx, col+dy)
            return result

        count = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] and dfs(row, col)%k == 0:
                    count += 1
        return count