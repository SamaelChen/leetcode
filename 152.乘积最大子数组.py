#
# @lc app=leetcode.cn id=152 lang=python3
#
# [152] 乘积最大子数组
#
# %%
# @lc code=start
class Solution:
    def maxProduct(self, nums) -> int:
        pos, neg = nums.copy(), nums.copy()
        for i, num in enumerate(nums):
            if i > 0:
                pos[i] = max(pos[i], 0, pos[i-1]*num, neg[i-1]*num)
                neg[i] = min(neg[i], 0, pos[i-1]*num, neg[i-1]*num)
        return max(pos)
# @lc code=end
# %%
