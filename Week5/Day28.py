# 122 Best Time to Buy and Sell Stock II
# count only positive days

# 55 Jump Game
# for i = 0; i <= cover
# python不支持动态修改for循环中变量,使用while循环代替
# more practice

# 45 Jump Game II
# more practice
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        cur, reach = 0, 0
        jump = 0
        for i in range(len(nums)):
            reach = max(reach, i + nums[i])
            # at the furtherest cur
            if i == cur:
                # if not there add one step, update furtherest reach
                if cur < len(nums) - 1:
                    cur = reach
                    jump += 1
                if reach >= len(nums) - 1:
                    break
        return jump

# 1005 Maximize Sum of Array After K Negations
# remove all negatives then flip the smallest