class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        res = 0

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def bfs(r, c):
            q = deque()
            grid[r][c] = "0"
            q.append((r, c))

            while q:
                q_len = len(q)
                for _ in range(q_len):
                    r, c = q.popleft()

                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if (nr < 0 or nr >= ROWS or nc < 0 
                            or nc >= COLS or grid[nr][nc] == "0"):
                            continue
                        q.append((nr, nc))
                        grid[nr][nc] = "0"

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    bfs(r, c)
                    res += 1
        return res