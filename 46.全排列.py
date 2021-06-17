#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#
# %%
# @lc code=start
class Solution:
    def permute(self, nums):
        n = len(nums)
        def backtrack(path, nums):
            if len(path) == n:
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