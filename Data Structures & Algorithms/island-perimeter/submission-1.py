class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        res = 0 

        ROWS, COLS = len(grid), len(grid[0])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    sides = 4
                    if (r > 0 and grid[r - 1][c] == 1):
                        sides -= 2
                    if (c > 0 and grid[r][c - 1] == 1):
                        sides -= 2
                    res += sides
        return res