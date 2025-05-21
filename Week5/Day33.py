# 62 Unique Paths
# 二刷
# use table for memorization
# DP
# grid[i][j] = grid[i][j-1] + grid[i-1][j]
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0 for _ in range(n)] for _ in range(m)]

        # initialization
        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1
        # print(dp)
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[m-1][n-1]

# recursive
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        return self.traversal(m-1,n-1)
    
    def traversal(self, row, col):
        if row == 0 or col == 0:
            return 1
        if row < 0 or col < 0:
            return 0
        
        return self.traversal(row-1, col) + self.traversal(row, col-1)

# 63 Unique Paths II
# obstacle remove possibilities from one side

# 343 Integer Break
# dp[2] = 1
# max(dp[i-j]*j, (i-j)*j, dp[i])
# 二刷


