# 647 Palindromic Substrings
# method 1: dp
# dp[i][j] is palin when dp[i+1][j-1] is also palin
# 注意遍历顺序
class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        result = 0

        for i in range(len(s)-1, -1, -1):
            for j in range(i, len(s)):
                if s[i] == s[j]:
                    if j - i <= 1:
                        # 相邻
                        # print(i, j, '+')
                        dp[i][j] = True
                        result += 1
                    elif dp[i+1][j-1] == True:
                        # print(i, j)
                        dp[i][j] = True
                        result += 1
        
        return result
# method 2: two pointers

# 516
# dp summary