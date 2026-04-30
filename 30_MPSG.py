class Solution:
    def solver(self, i, j, cost, grid, k, dp):

        m, n = len(grid), len(grid[0])
        if i >= m or j >= n:
            return -1e9

        add_cost = 0 if grid[i][j] == 0 else 1
        score = grid[i][j]

        if cost + add_cost > k:
            return -1e9

        if i == m - 1 and j == n - 1:
            return grid[i][j]

        if dp[i][j][cost + add_cost] != -1:
            return dp[i][j][cost + add_cost]

        best = max(self.solver(i + 1, j, cost + add_cost, grid, k, dp), self.solver(i, j + 1, cost + add_cost, grid, k, dp))

        dp[i][j][cost + add_cost] = -1e9 if best == -1e9 else best + score

        return dp[i][j][cost + add_cost]


    def maxPathScore(self, grid, k):

        m, n = len(grid), len(grid[0])

        dp = [[[-1 for _ in range(k + 1)] for _ in range(n + 1)] for _ in range(m + 1)]

        res = self.solver(0, 0, 0, grid, k, dp)

        if res == -1e9:
            return -1
        return res