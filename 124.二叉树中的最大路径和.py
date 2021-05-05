#
# @lc app=leetcode.cn id=124 lang=python3
#
# [124] 二叉树中的最大路径和
#
# %%
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root):
        if root is None:
            return 0
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        self.maxSum = max(self.maxSum, (left + right + root.val))
        return max(0, max(left, right) + root.val)
    def maxPathSum(self, root: TreeNode) -> int:
        self.maxSum = float('-inf')
        _ = self.dfs(root)
        return self.maxSum
# @lc code=end
# %%
