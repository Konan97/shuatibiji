# 322 Coin Change
# dp[j] the least number to get value j
# dp[j] = min(dp[j], dp[j-coin]+1)

# 279 Perfect Square
# same as 322 
# dp[j] = min(dp[j], dp[j-i*i]+1)

# 139 Word Break
# permutation so 先背包 再物品
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dp = [False for _ in range(len(s)+1)]
        dp[0] = True
        # 背包
        for j in range(len(s)+1):
            # 物品
            for i in range(j, len(s)+1):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
        
        return dp[len(s)]
