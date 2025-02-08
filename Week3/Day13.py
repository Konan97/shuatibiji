# 226 Invert Binary Tree
class Solution(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        if not root: return None
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

# 101 Symmetric Tree
# return type boolean
# stop conditions
# single actions: left.left = right.right ....

# 104 Max depth of Binary Tree
# 1 + max(left, right)

# 111 Minimum Depth of Binary Tree
# leaf node is both left and right are none

# 222 Count Complete Tree Nodes
# 1 + left + right

# 110 Balanced Binary Tree
# need more practice
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if self.check(root) != -1:
            return True
        return False

    
    def check(self, root):
        if not root:
            return 0
        left = self.check(root.left)
        if left == -1:
            return -1
        right = self.check(root.right)
        if right == -1:
            return -1
        
        if abs(left - right) > 1:
            return -1
        else:
            return 1 + max(left, right)