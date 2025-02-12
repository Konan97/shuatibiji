# 513 Find Bottom Left Tree Value
# level traversal 

# 112 Path Sum
# more practice
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        if not root: return False
        return self.traversal(root, targetSum - root.val)

    def traversal(self, root, count):
        # stop condition
        # leave and count = 0
        if not root.left and not root.right and count == 0:
            return True
        # leave
        if not root.left and not root.right:
            return False
        
        if root.left:
            count -= root.left.val
            if self.traversal(root.left, count):
                return True
            count += root.left.val
        if root.right:
            count -= root.right.val
            if self.traversal(root.right, count):
                return True
            count += root.right.val
        return False

        
# 106 Construct Binary Tree from Inorder and postorder traversal
# a very good problem need more practice
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: Optional[TreeNode]
        """
        if len(postorder) == 0:
            return None
        rootVal = postorder[-1]
        root = TreeNode(rootVal, None, None)
        if len(postorder) == 1:
            return root
        i = 0
        for i in range(len(inorder)):
            if inorder[i] == rootVal:
                break
        # split inorder
        leftIn = inorder[0:i]
        rightIn = inorder[i+1:len(inorder)]
        #print(leftIn, rightIn)

        # split postorder
        leftPost = postorder[0:len(leftIn)]
        rightPost = postorder[len(leftIn):len(postorder)-1]
        #print(leftPost, rightPost)

        root.left = self.buildTree(leftIn, leftPost)
        root.right = self.buildTree(rightIn, rightPost)
        return root

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

# 530 Minimum absolute Difference in BST
# inorder traversal find min diff
