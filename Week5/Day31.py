# 56 Merge Intervals
# find the cur max right
# if left > cur max right, then new overlapping interval


# 738 Monotone Increasing Digits
# if n[i] < n[i-1], n[i - 1] -= 1 make n[i] = 9 and flag i

# 968 Binary Tree Cameras
# Postorder traversal 从下往上
# 0 no cover 1 camera 2 cover
# both covered parent no cover
# if one is uncovered, parent camera
# if one is camera, parent is covered

# 484 Find Permutation
# stack or reverse array
class Solution(object):
    def findPermutation(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        stack = []
        res = []

        for i in range(len(s)):
            if s[i] == "I":
                res.append(i+1)
                while stack:
                    res.append(stack[-1])
                    stack.pop(-1)
            elif s[i] == "D":
                stack.append(i+1)
        stack.append(len(s)+1)        
        while stack:
            res.append(stack[-1])
            stack.pop(-1)

        return res