# 1049 Last Stone Weight
# same as 416
# make stones reach sum/2
# 二刷


# 494 Target Sum
# 找背包组合
# more practice
# dp[j] += dp[j-nums[i]]

# 474 Ones and Zeros
# 2D backpack of ones and zeros
# not easy
class Solution(object):
    def findMaxForm(self, strs, m, n):
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
                # 物品
        for string in strs:
            count0, count1 = 0, 0
            for s in string:
                if s == "1":
                    count1 += 1
                if s == "0":
                    count0 += 1
            # 背包
            for i in range(m, count0-1, -1):
                for j in range(n, count1-1, -1):
                    dp[i][j] = max(dp[i][j], dp[i-count0][j-count1] + 1)

        return dp[m][n]