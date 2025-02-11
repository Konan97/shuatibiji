# 501 Find Mode in Binary Search Tree
# inorder then map

# 236 Lowest Common Ancestor of a Binary Tree
# search one branch:
'''if traversal(root.right): return'''
# search entire tree
'''left = traversal(root.left)
   right = traversal(root.right)
   return left .... right'''