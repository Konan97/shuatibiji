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
# 257 Binary Tree Paths
# more practice
# preorder
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[str]
        """
        res = []
        self.traversal(root, [], res)
        return res

    def traversal(self, root, path, res):

        path.append(str(root.val)) # middle
        # stop condition
        if not root.left and not root.right:
            res.append("->".join(path))
            return
        # left
        if root.left:
            self.traversal(root.left, path, res)
            path.pop()
        # right
        if root.right:
            self.traversal(root.right, path, res)
            path.pop()
        

            
# 404 Sum of left leaves
# more practice
# postorder
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        left = self.sumOfLeftLeaves(root.left) # left
        # find left leaves
        if root.left and not root.left.left and not root.left.right:
            left = root.left.val
        right = self.sumOfLeftLeaves(root.right) # right
        sum = left + right # mid
        return sum

        