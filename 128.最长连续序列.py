#
# @lc app=leetcode.cn id=128 lang=python3
#
# [128] 最长连续序列
#
# %%
# @lc code=start
class UnionFind:
    def __init__(self, n):
        self.parents = {num: num for num in n}
        self.size = {num: 1 for num in n}
    def union(self, x, y):
        xroot = self.find(x)
        yroot = self.find(y)
        if xroot != yroot:
            if self.size[xroot] < self.size[yroot]:
                self.parents[xroot] = yroot
                self.size[yroot] += self.size[xroot]
            else:
                self.parents[yroot] = xroot
                self.size[xroot] += self.size[yroot]
    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]


class Solution:
    def longestConsecutiveBrutal(self, nums) -> int:
        # nums = list(set(nums))
        nums = sorted(nums)
        if len(nums) == 1:
            return 1
        length = 1
        max_length = 0
        for num1, num2 in zip(nums[:-1], nums[1:]):
            if num2 - num1 == 1:
                length += 1
            else:
                length = 1
            max_length = max(max_length, length)
        return max_length
        
    def longestConsecutive(self, nums) -> int:
        uf = UnionFind(nums)
        res = 0
        for num in nums:
            if num - 1 in uf.parents:
                uf.union(num-1, num)
            if num + 1 in uf.parents:
                uf.union(num+1, num)
            res = max(res, uf.size[uf.parents[num]])
        return res
# @lc code=end
# %%
# s = Solution()
# s.longestConsecutiveBrutal([0, 0])
# %%
