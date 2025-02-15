# 530 Minimum absolute Difference in BST
# inorder traversal find min diff
 

# 501 Find Mode in Binary Search Tree
# inorder then map

# 236 Lowest Common Ancestor of a Binary Tree
# search one branch:
'''if traversal(root.right): return'''
# search entire tree
'''left = traversal(root.left)
   right = traversal(root.right)
   return left .... right'''
# 如果left 和 right都不为空，说明此时root就是最近公共节点。这个比较好理解
# 如果left为空，right不为空，就返回right，说明目标节点是通过right返回的，反之依然。
# postorder traversal

