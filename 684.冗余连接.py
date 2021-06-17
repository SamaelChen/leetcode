#
# @lc app=leetcode.cn id=684 lang=python3
#
# [684] 冗余连接
#
# %%
# @lc code=start
class Solution:
    def findRedundantConnection(self, edges):
        self.parents = {}
        self.size = {}
        def make_set(x):
            self.parents[x] = x
            self.size[x] = 1
        for e in edges:
            p, c = e[0], e[1]
            if p not in self.parents:
                make_set(p)
            if c not in self.parents:
                make_set(c)
        def find(x):
            if self.parents[x] == x:
                return x
            else:
                self.parents[x] = find(self.parents[x])
                return self.parents[x]
        def union(x, y):
            xroot = find(x)
            yroot = find(y)
            if xroot != yroot:
                if self.size[xroot] > self.size[yroot]:
                    large = xroot
                    small = yroot
                else:
                    large = yroot
                    small = xroot
                self.parents[small] = large
                self.size[large] += self.size[small]
        def is_connected(x, y):
            if find(x) == find(y):
                return True
            else:
                union(x, y)
        
        for e in edges:
            if is_connected(e[0], e[1]):
                return e
# @lc code=end
# %%
# s = Solution()
# s.findRedundantConnection([[1, 2], [1, 3], [2, 3]])
# %%
