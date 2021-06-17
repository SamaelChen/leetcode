#
# @lc app=leetcode.cn id=41 lang=python3
#
# [41] 缺失的第一个正数
#
# %%
# @lc code=start
class Solution:
    def firstMissingPositive(self, nums):
        i = 1
        while i in nums:
            i += 1
        return i 
# @lc code=end