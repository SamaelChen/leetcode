#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#
# %%
# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.res = []
    def inorderTraversal(self, root):
        if root is None:
            return []
        self.inorderTraversal(root.left)
        if root.val:
            self.res.append(root.val)
        self.inorderTraversal(root.right)
        return self.res
        
# %%
class Solution:
    def inorderTraversal(self, root):
        inorder = []
        node = root
        path = []
        while node or path:
            if node:
                path.append(node)
                node = node.left
            else:
                node = path.pop()
                inorder.append(node.val)
                node = node.right
        return inorder

        
# @lc code=end

# %%
tree = TreeNode(1)
tree.left = TreeNode(2)
tree.left.right = TreeNode(7)
tree.right = TreeNode(3)
tree.right.left = TreeNode(4)
tree.right.right = TreeNode(5)
tree.right.left.left = TreeNode(6)
# %%
s = Solution()
s.postorderTraversal(tree)
# %%
