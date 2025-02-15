# 235 Lowest Common Ancestor of a Binary Search Tree
#
# 701 Insert into a Binary Search Tree
# insert whenever root == None:
# return node then root.left, root.right
class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: Optional[TreeNode]
        :type val: int
        :rtype: Optional[TreeNode]
        """
        if not root:
            node = TreeNode(val, None, None)
            return node
        if root.val > val:
            root.left = self.insertIntoBST(root.left, val)
        elif root.val <= val:
            root.right = self.insertIntoBST(root.right, val)
    
        return root
