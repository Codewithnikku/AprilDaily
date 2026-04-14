class Solution:
    def minimumTotalDistance(self, robot, factory):
        robot.sort()
        factory.sort()
        pos = []
        for p, limit in factory:
            pos.extend([p] * limit)
        
        m, n = len(robot), len(pos)
        dp = [[float('inf')] * (n + 1) for _ in range(m + 1)]
        
        for j in range(n + 1):
            dp[0][j] = 0
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = dp[i][j - 1]
                dp[i][j] = min(dp[i][j], dp[i - 1][j - 1] + abs(robot[i - 1] - pos[j - 1]))
        
        return dp[m][n]