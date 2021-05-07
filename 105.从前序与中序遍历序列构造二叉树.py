#
# @lc app=leetcode.cn id=105 lang=python3
#
# [105] 从前序与中序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder) == 0:
            return None
        if len(preorder) == 1:
            return TreeNode(preorder[0])
        root = TreeNode(preorder[0])
        for idx, x in enumerate(inorder):
            if x == preorder[0]:
                left = inorder[:idx]
                right = inorder[(idx+1):]
                break
        root.left = self.buildTree(preorder[1:len(left)+1], left)
        root.right = self.buildTree(preorder[(len(preorder) - len(right)):], right)
        return root
# @lc code=end

