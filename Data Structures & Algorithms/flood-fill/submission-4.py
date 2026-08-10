class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        ROWS, COLS = len(image), len(image[0])

        originalColor = image[sr][sc]

        image[sr][sc] = color

        visited = set()

        visited.add((sr, sc))

        q = deque()

        q.append((sr, sc))

        directions = [[1, 0], [-1, 0], [0, -1], [0, 1]]

        while q:
            r, c = q.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if (nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS or (nr, nc) in visited 
                    or image[nr][nc] != originalColor):
                    continue
                image[nr][nc] = color
                visited.add((nr, nc))
                q.append((nr, nc))
        return image

