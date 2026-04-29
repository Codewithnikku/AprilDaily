class Solution(object):
    def maximumAmount(self, coins):
        m, n = len(coins), len(coins[0])
        
        # dp[i][j][k]: max money at (i,j) with k skips used
        dp = [[[-float('inf')] * 3 for _ in range(n)] for _ in range(m)]
        
        # Initialize start
        for k in range(3):
            if coins[0][0] >= 0:
                dp[0][0][k] = coins[0][0]
            else:
                # take negative
                dp[0][0][k] = coins[0][0]
                # skip if allowed
                if k > 0:
                    dp[0][0][k] = max(dp[0][0][k], 0)
        
        # Fill DP
        for i in range(m):
            for j in range(n):
                for k in range(3):
                    if i == 0 and j == 0:
                        continue
                    
                    val = coins[i][j]
                    
                    # From top
                    if i > 0:
                        # Take
                        dp[i][j][k] = max(dp[i][j][k], dp[i-1][j][k] + val)
                        
                        # Skip if negative
                        if val < 0 and k > 0:
                            dp[i][j][k] = max(dp[i][j][k], dp[i-1][j][k-1])
                    
                    # From left
                    if j > 0:
                        # Take
                        dp[i][j][k] = max(dp[i][j][k], dp[i][j-1][k] + val)
                        
                        # Skip if negative
                        if val < 0 and k > 0:
                            dp[i][j][k] = max(dp[i][j][k], dp[i][j-1][k-1])
        
        return max(dp[m-1][n-1])