class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        
        cnt = 0
        n, m = len(grid), len(grid[0])

        row = [0]*n
        col = [0]*m
        # the answer will be count every thing in row and col then add these if the count is reater than 1 then we have to cnstruct servers counted twice it will be counted in 
        rows = set()
        cols = set()

        for i in range(n):
            prev = tuple()
            for j in range(m):
                if grid[i][j]:
                    if prev:
                        # count current and prev
                        rows.add(prev)
                        rows.add((i, j))
                    else:
                        prev = (i, j)
        for j in range(m):
            prev = ()
            for i in range(n):
                if grid[i][j]:
                    if prev:
                        cols.add(prev)
                        cols.add((i, j))
                    else:
                        prev = (i, j)
        
        return len(rows) + len(cols) - len(rows & cols)

