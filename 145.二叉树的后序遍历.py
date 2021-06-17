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
a = '{"04202012247c0564174":{"goodsCode":"04202012247c0564174","goodsCount":5,"goodsId":"86D4479351B60B3FDEEC40B0","goodsName":"农夫山泉维他命水热带水果风味500ml"},"04202012246506b8464":{"goodsCode":"04202012246506b8464","goodsCount":4,"goodsId":"86D4479351B60B3FD3073139","goodsName":"美天黄桃燕麦酸奶180g"},"04202012043bb7bd233":{"goodsCode":"04202012043bb7bd233","goodsCount":5,"goodsId":"863B234A09740B257F5A27E6","goodsName":"统一阿萨姆奶茶饮料500ml"},"042020122464f0bf6c4":{"goodsCode":"042020122464f0bf6c4","goodsCount":15,"goodsId":"86D4479351B60B3FD3073137","goodsName":"美天全脂巴氏杀菌乳180g"},"04202012247bfb2b3d4":{"goodsCode":"04202012247bfb2b3d4","goodsCount":12,"goodsId":"86D4479351B60B3FDEEC40AF","goodsName":"怡宝饮用纯净水550ml"},"0420201204750dc7be3":{"goodsCode":"0420201204750dc7be3","goodsCount":4,"goodsId":"863B234A09740B257FBA2867","goodsName":"百事可乐可乐型汽水600ml"},"042020122464df0c044":{"goodsCode":"042020122464df0c044","goodsCount":5,"goodsId":"86D4479351B60B3FD3073135","goodsName":"美天咖啡酸奶120g"}}'

# %%
import pandas as pd
# %%
b = pd.read_json(a, orient='index')
# %%
b
# %%
b.to_json(orient='records')
# %%
