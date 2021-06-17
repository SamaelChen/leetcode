#
# @lc app=leetcode.cn id=137 lang=python3
#
# [137] 只出现一次的数字 II
#
# %%
# @lc code=start
class Solution:
    def singleNumber(self, nums) -> int:
        a, b = 0, 0
        for num in nums:
            a = ~ b & (a ^ num)
            b = ~ a & (b ^ num)
        return a
# @lc code=end
# %%
