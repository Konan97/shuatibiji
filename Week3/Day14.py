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

        