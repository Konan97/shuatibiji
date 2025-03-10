# 300 Longest Increasing Subsequence
def lengthOfLIS(self, nums):
        dp = [1 for _ in range(len(nums))]
        
        for i in range(len(nums)):
            for j in range(0, i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j]+1) # make dp[i] bigger
            print(dp)
        return max(dp)

# 674 Longest Continuous Increasing Subsequence
# single layer dp
def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [1 for _ in range(len(nums))]

        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                dp[i] = dp[i-1]+1
        
        return max(dp)

# 718 Maximum length of Repeated Subarray
# 