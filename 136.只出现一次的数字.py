#
# @lc app=leetcode.cn id=136 lang=python3
#
# [136] 只出现一次的数字
#
# %%
# @lc code=start
class Solution:
    def singleNumber(self, nums) -> int:
        res = 0
        for num in nums:
            res ^= num
        return res
# @lc code=end


# %%
# s = Solution()
# s.singleNumber([4, 1, 2, 2, 1])
# %%
