class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        rowscount, colscount = [0] * ROWS, [0] * COLS

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]:
                    rowscount[r] += 1
                    colscount[c] += 1
        print(rowscount)
        
        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                if (grid[r][c] and max(rowscount[r], colscount[c]) > 1):
                    res += 1
        return res

