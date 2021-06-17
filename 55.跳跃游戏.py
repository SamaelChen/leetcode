#
# @lc app=leetcode.cn id=55 lang=python3
#
# [55] 跳跃游戏
#
# %%
# @lc code=start
class Solution:
    def canJump(self, nums):
        if len(nums) == 1:
            return True
        end, max_position = 0, 0
        for i in range(len(nums) - 1):
            max_position = max(max_position, nums[i] + i)
            if max_position >= len(nums) - 1:
                return True
            if i == end:
                if nums[i] == 0 and max_position == end:
                    return False
                end = max_position
        if max_position < len(nums) - 1:
            return False
# @lc code=end
# %%
