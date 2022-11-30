#
# @lc app=leetcode.cn id=145 lang=python3
#
# [145] 二叉树的后序遍历
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

    def postorderTraversal(self, root):
        if not root:
            return []
        self.postorderTraversal(root.left)
        self.postorderTraversal(root.right)
        if root.val:
            self.res.append(root.val)
        return self.res
# @lc code=end


# %%
class Solution:
    def postorderTraversal(self, root):
        postorder = []
        visited = None
        path = []
        node = root
        while node or path:
            if node:
                path.append(node)
                node = node.left
            else:
                last_node = path[-1]
                if last_node.right and last_node.right != visited:
                    node = last_node.right
                else:
                    visited = path.pop()
                    postorder.append(visited.val)
        return postorder


# %%
s = Solution()
s.postorderTraversal(tree)

# %%
