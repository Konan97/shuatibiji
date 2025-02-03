# 144 Binary Tree Preorder Traversal
# recursive
# 中左右

# 145 Postorder Traversal
# 左右中
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        self.postTra(root, res)
        return res
        
    def postTra(self, root, res):
        if not root:
            return
        self.postTra(root.left, res)
        self.postTra(root.right, res)
        res.append(root.val)