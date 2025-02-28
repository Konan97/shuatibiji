# 654 Maximum Binary Tree
# same as 106
class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: Optional[TreeNode]
        """
        if len(nums) == 0:
            return None
        # find root
        rootVal = max(nums)
        root = TreeNode(rootVal, None, None)
        if len(nums) == 1:
            return root
        # break left and right side
        i = 0
        for i in range(len(nums)):
            if nums[i] == rootVal:
                break
        left = nums[0:i]
        right = nums[i+1:len(nums)]
        # print(left, right)
        root.left = self.constructMaximumBinaryTree(left)
        root.right = self.constructMaximumBinaryTree(right)
        return root

# 617 Merge two binary tree
# if not root1 return root2
# if not root2 return root1

# 700 Search in a Binary Search Tree
# if not root or root.val == val return root

# 98 Validate Binary Search Tree
# inorder traversal BST gives a sorted array
# 左中右
