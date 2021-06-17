#
# @lc app=leetcode.cn id=47 lang=python3
#
# [47] 全排列 II
#
# %%
# @lc code=start
class Solution:
    def permuteUnique(self, nums):
        n = len(nums)
        def backtrack(path, nums):
            if len(path) == n and path not in res:
                res.append(path[:])
            for i in range(len(nums)):
                path.append(nums[i])
                current = nums[:i] + nums[(i+1):]
                backtrack(path, current)
                path.pop()
        res = []
        backtrack([], nums)
        return res
# @lc code=end
# %%
