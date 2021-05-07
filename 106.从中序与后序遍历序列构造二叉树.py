#
# @lc app=leetcode.cn id=106 lang=python3
#
# [106] 从中序与后序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if len(postorder) == 0:
            return None
        if len(postorder) == 1:
            return TreeNode(postorder[-1])
        root = TreeNode(postorder[-1])
        for idx, x in enumerate(inorder):
            if x == postorder[-1]:
                left = inorder[:idx]
                right = inorder[(idx+1):]
                break
        root.left = self.buildTree(left, postorder[:len(left)])
        root.right = self.buildTree(right, 
                                    postorder[-(len(right)+1):-1])
        return root
# @lc code=end
# %%
