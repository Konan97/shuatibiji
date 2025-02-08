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