#
# @lc app=leetcode.cn id=721 lang=python3
#
# [721] 账户合并
#
# %%
# @lc code=start
import collections


class UnionFind:
    def __init__(self, nodes) -> None:
        self.parents = list(range(nodes))
    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    def union(self, x, y):
        self.parents[self.find(y)] = self.find(x)

class Solution:
    def accountsMerge(self, accounts):
        email2idx = {}
        email2name = {}
        for acc in accounts:
            name = acc[0]
            for email in acc[1:]:
                if email not in email2idx:
                    email2idx[email] = len(email2idx)
                    email2name[email] = name
        uf = UnionFind(len(email2idx))
        for acc in accounts:
            firstIdx = email2idx[acc[1]]
            for email in acc[2:]:
                uf.union(firstIdx, email2idx[email])
        idx2email = collections.defaultdict(list)
        for email, idx in email2idx.items():
            idx = uf.find(idx)
            idx2email[idx].append(email)
        res = []
        for emails in idx2email.values():
            res.append([email2name[emails[0]]] + sorted(emails))
        return res

# @lc code=end
# %%
s = Solution()
s.accountsMerge([["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"],
                 ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]])
# %%
