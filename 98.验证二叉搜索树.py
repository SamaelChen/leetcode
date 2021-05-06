#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if root is None:
            return True
        res, que = [], []
        curr = root
        while curr is not None or len(que) > 0:
            if curr is not None:
                que.append(curr)
                curr = curr.left
            else:
                curr = que.pop()
                res.append(curr.val)
                curr = curr.right
        res_sort = res.copy()
        res_sort.sort()
        if res == res_sort and len(set(res)) == len(res):
            return True
        else:
            return False
# @lc code=end
# %%
