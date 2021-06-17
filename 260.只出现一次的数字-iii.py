#
# @lc app=leetcode.cn id=260 lang=python3
#
# [260] 只出现一次的数字 III
#
# %%
# @lc code=start
class Solution:
    def singleNumber(self, nums):
        eor = 0
        for num in nums:
            eor ^= num
        div = eor & (- eor)
        res = 0
        for num in nums:
            if num & div:
                res ^= num
        return [res, res ^ eor]
# @lc code=end
# %%
