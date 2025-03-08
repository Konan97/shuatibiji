# 198 House Robber
# dp[i] = max(dp[i-1], dp[i-2]+nums[i])

# 213 House Robber II
# same as 198
# do both [0:n-1] and [1:n]

# 337 House Robber III
# dp Btree
class Solution(object):
    def rob(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        return max(self.robTree(root))
        
        
    def robTree(self, node):
        if not node: return [0,0]

        # traversal
        leftDp = self.robTree(node.left)
        rightDp = self.robTree(node.right)

        # mid
        rob = node.val + leftDp[0] + rightDp[0]
        noRob = max(leftDp) + max(rightDp)

        return [noRob, rob]