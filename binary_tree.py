# %%
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# %%
def generateTree(lst):
    if len(lst) == 0:
        return None
    que = []
    fill_left = True
    for ele in lst:
        if ele is not None:
            node = TreeNode(ele)
        else:
            node = None
        if len(que) == 0:
            que.append(node)
            root = que[0]
            root.val = ele
        elif fill_left:
            que[0].left = node
            fill_left = False
            if node is not None:
                que.append(node)
        else:
            que[0].right = node
            fill_left = True
            que = que[1:]
            if node is not None:
                que.append(node)
    return root
# %%
lst = [1, 2, 3, None, 4, 5, 6]
tree = generateTree(lst)
# %%
# recursive
class recursiveSolution:
    def __init__(self):
        self.res = []
    def preorder(self, root):
        if root is None:
            return
        if root.val:
            self.res.append(root.val)
        self.preorder(root.left)
        self.preorder(root.right)
        return self.res

    def inorder(self, root):
        if root is None:
            return
        self.inorder(root.left)
        if root.val:
            self.res.append(root.val)
        self.inorder(root.right)
        return self.res

    def postorder(self, root):
        if root is None:
            return
        self.postorder(root.left)
        self.postorder(root.right)
        if root.val:
            self.res.append(root.val)
        return self.res
# %%
s = recursiveSolution()
print(s.preorder(tree))
s = recursiveSolution()
print(s.inorder(tree))
s = recursiveSolution()
print(s.postorder(tree))
# %%
# Not recursive

def preorder(root):
    if root is None:
        return
    res, que = [], [root]
    while len(que) > 0:
        curr = que.pop()
        if curr.val:
            res.append(curr.val)
        if curr.right is not None:
            que.append(curr.right)
        if curr.left is not None:
            que.append(curr.left)
    return res


def inorder(root):
    if root is None:
        return
    res, que = [], []
    curr = root
    while len(que) > 0 or curr is not None:
        if curr is not None:
            que.append(curr)
            curr = curr.left
        else:
            curr = que.pop()
            if curr.val is not None:
                res.append(curr.val)
            curr = curr.right
    return res


def postorder(root):
    if root is None:
        return
    res, que = [], []
    curr, lastvisit = root, None
    while len(que) > 0 or curr is not None:
        if curr is not None:
            que.append(curr)
            curr = curr.left
        else:
            if lastvisit != que[-1].right and que[-1].right is not None:
                curr = que[-1].right
            else:
                if que[-1].val is not None:
                    res.append(que[-1].val)
                lastvisit = que.pop()
    return res
# %%
print(preorder(tree))
print(inorder(tree))
print(postorder(tree))
# %%
# DFS
class DFS:
    def __init__(self):
        self.res = []
    def preorder(self, root):
        if root is None:
            return
        if root.val is not None:
            self.res.append(root.val)
        self.preorder(root.left)
        self.preorder(root.right)
        return self.res


class BFS:
    def levelOrder(self, root):
        if root is None:
            return
        res, que = [], [root]
        while len(que) > 0:
            for curr in que:
                res.append(curr.val)
                que = que[1:]
                if curr.left is not None:
                    que.append(curr.left)
                if curr.right is not None:
                    que.append(curr.right)
        return res
# %%
s = DFS()
s.preorder(tree)
# %%
s = BFS()
s.levelOrder(tree)
# %%
# leetcode practice

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
# %%
s = Solution()
print(s.maxDepth(tree))
print(s.isBalanced(tree))
# %%
tree2 = generateTree([1, 2, 2, 3, None, None, 3, 4, None, None, 4])
# %%
print(s.isBalanced(tree2))
# %%
# max path sum
# 思路上，最小的一个完整二叉树是一个根节点两个叶子结点，根节点最大和的路径就是根节点的值加上左，右中最大的一个
# 考虑到负数的路径不采纳，所以最小是0

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
# %%
s = Solution()
s.maxPathSum(tree)
# %%
# check if it is a valid binary search tree
class Solution():
    def isValidBST(self, root: TreeNode) -> bool:
        if root is None:
            return True
        def valid_min_max(node):
            isvalid = True
            if node.left is not None:
                l_isvalid, l_min, l_max = valid_min_max(node.left)
                isvalid = isvalid and node.val > l_max
            else:
                l_isvalid, l_min = True, node.val
            
            if node.right is not None:
                r_isvalid, r_min, r_max = valid_min_max(node.right)
                isvalid = isvalid and node.val < r_min
            else:
                r_isvalid, r_max = True, node.val
            return l_isvalid and r_isvalid and isvalid, l_min, r_max
        return valid_min_max(root)[0]

# %%
lst = [5, 4, 6, None, None, 3, 7]
tree = generateTree(lst)
s = Solution()
s.isValidBST(tree)

# %%
