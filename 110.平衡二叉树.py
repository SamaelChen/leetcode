#
# @lc app=leetcode.cn id=110 lang=python3
#
# [110] 平衡二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        return 1+max(self.maxDepth(root.left), self.maxDepth(root.right))

    def isBalanced(self, root: TreeNode) -> bool:
        if root is None:
            return True
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        depth_diff = abs(left_depth - right_depth)
        return depth_diff <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)

# @lc code=end

