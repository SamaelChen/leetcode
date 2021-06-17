#
# @lc app=leetcode.cn id=144 lang=python3
#
# [144] 二叉树的前序遍历
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
    def __init__(self):
        self.res = []
    def preorderTraversal(self, root):
        if not root:
            return []
        if root.val:
            self.res.append(root.val)
        self.preorderTraversal(root.left)
        self.preorderTraversal(root.right)
        return self.res
        
# @lc code=end


# %%
class Solution:
    def preorderTraversal(self, root):
        preorder = []
        if root is None:
            return preorder
        path = [root]
        while len(path) > 0:
            node = path.pop()
            preorder.append(node.val)
            if node.right:
                path.append(node.right)
            if node.left:
                path.append(node.left)
        return preorder
