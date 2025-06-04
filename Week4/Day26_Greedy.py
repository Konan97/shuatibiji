# Greedy Algorithm
# 455 Assign Cookies
# loop greed array

# 376 Wiggle Subsequence
class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        diff = [0]
        for i in range(1, len(nums)):
            if diff and ((diff[-1] >= 0 and nums[i] - nums[i-1] < 0) or (diff[-1] <= 0 and nums[i] - nums[i-1] > 0)):
                diff.append(nums[i] - nums[i-1])
        # print(diff)
        return len(diff)

# 53 Maximum Subarray
# if curSum < 0: update startIndex
