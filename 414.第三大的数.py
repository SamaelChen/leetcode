#
# @lc app=leetcode.cn id=414 lang=python3
#
# [414] 第三大的数
#
# %%
# @lc code=start
class Solution:
    def thirdMax(self, nums) -> int:
        nums = list(set(nums))
        nums.sort()
        if len(nums) >= 3:
            return nums[-3]
        else:
            return nums[-1]
# @lc code=end

# %%
