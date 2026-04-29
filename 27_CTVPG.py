class Solution(object):
    def hasValidPath(self, grid):
        m, n = len(grid), len(grid[0])

        directions = {
            1: [(0, -1), (0, 1)],
            2: [(-1, 0), (1, 0)],
            3: [(0, -1), (1, 0)],
            4: [(0, 1), (1, 0)],
            5: [(0, -1), (-1, 0)],
            6: [(0, 1), (-1, 0)]
        }

        visited = [[False]*n for _ in range(m)]
        stack = [(0, 0)]
        visited[0][0] = True

        while stack:
            x, y = stack.pop()
            if x == m - 1 and y == n - 1:
                return True

            for dx, dy in directions[grid[x][y]]:
                nx, ny = x + dx, y + dy

                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                    if (-dx, -dy) in directions[grid[nx][ny]]:
                        visited[nx][ny] = True
                        stack.append((nx, ny))

        return False