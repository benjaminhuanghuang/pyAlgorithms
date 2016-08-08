'''
337. House Robber III

The thief has found himself a new place for his thievery again.
There is only one entrance to this area, called the "root."
Besides the root, each house has one and only one parent house.
After a tour, the smart thief realized that "all houses in this place forms a binary tree".
It will automatically contact the police if two directly-linked houses were broken into on the same night.

Determine the maximum amount of money the thief can rob tonight without alerting the police.

Example 1:
     3
    / \
   2   3
    \   \
     3   1
Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
Example 2:
     3
    / \
   4   5
  / \   \
 1   3   1
Maximum amount of money the thief can rob = 4 + 5 = 9.

# Hint:
rob_root = max(rob_L + rob_R , no_rob_L + no_nob_R + root.val)
no_rob_root = rob_L + rob_R

http://bookshadow.com/weblog/2016/03/13/leetcode-house-robber-iii/
'''


class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.dfs_rob(root)[0]

    def dfs_rob(self, root):
        if not root:
            return 0, 0
        rob_L, no_rob_L = self.dfs_rob(root.left)
        rob_R, no_rob_R = self.dfs_rob(root.right)
        return max(no_rob_L + no_rob_R + root.val, rob_L + rob_R), rob_L + rob_R


    def houseRobber3(self, root):
        rob, not_rob = self.visit(root)
        return max(rob, not_rob)

    def visit(self, root):
        if root is None:
            return 0, 0

        left_rob, left_not_rob = self.visit(root.left)
        right_rob, right_not_rob = self.visit(root.right)

        rob = root.val + left_not_rob + right_not_rob
        not_rob = max(left_rob, left_not_rob) + max(right_rob, right_not_rob)
        return rob, not_rob