#
# @lc app=leetcode.cn id=103 lang=python3
#
# [103] 二叉树的锯齿形层序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        l2r = True
        levels = []
        que = [root]
        while len(que) > 0:
            levels.append([])
            for node in que:
                levels[-1].append(node.val)
                que = que[1:]
                if node.left is not None:
                    que.append(node.left)
                if node.right is not None:
                    que.append(node.right)
            if not l2r:
                levels[-1] = levels[-1][::-1]
            l2r = not l2r
        return levels
# @lc code=end

