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

# 450 Delete Node in BST
# 5种情况 耐心debug add print
class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: Optional[TreeNode]
        :type key: int
        :rtype: Optional[TreeNode]
        """
        # not found
        if not root: return root
        
        if root.val == key:
            # node is a leave
            if not root.right and not root.left:
                return None
            # left is None
            elif not root.left and root.right:
                return root.right
            elif root.left and not root.right:
                return root.left
            # root is node, move left tree to the right tree left branch
            else:
                leftSide = root.left
                rightSide = root.right
                #print(leftSide.val, rightSide.val)
                while rightSide.left:
                    rightSide = rightSide.left
                # 耐心debug
                temp = rightSide
                #print(temp.val)
                temp.left = leftSide
                root = root.right
                return root
        root.left = self.deleteNode(root.left, key)
        root.right = self.deleteNode(root.right, key)
        return root
