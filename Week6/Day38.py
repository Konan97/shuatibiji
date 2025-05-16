# 322 Coin Change
# dp[j] the least number to get value j
# dp[j] = min(dp[j], dp[j-coin]+1)

# brute force
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        res = []
        self.backTrack(coins, amount, [], res)
        return min(res) if res else -1
    
    def backTrack(self, coins, amount, path, res):
        if sum(path) > amount:

            return
        elif sum(path) == amount:
            res.append(len(path))
            return
        
        for i in range(len(coins)):
            path.append(coins[i])
            print(path)
            self.backTrack(coins, amount, path, res)
            path.pop()

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
