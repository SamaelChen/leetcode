#
# @lc app=leetcode.cn id=45 lang=python3
#
# [45] 跳跃游戏 II
#
# %%
# @lc code=start
class Solution:
    def jumpPlagiarize(self, nums):
        if len(nums) <= 1:
            return 0
        elif len(nums) == 2:
            return 1
        steps, end, max_position = 0, 0, 0
        for i in range(0, len(nums)-1):
            max_position = max(max_position, nums[i] + i)
            if max_position >= len(nums) - 1:
                return steps + 1
            if i == end:
                end = max_position
                steps += 1
        return steps
    def jump(self, nums):
        if len(nums) <= 1:
            return 0
        elif len(nums) == 2:
            return 1
        max_position, step, step_max = 0, 0, 0
        for i in range(len(nums)):
            if step_max < i:
                step += 1
                step_max = max_position
            max_position = max(max_position, nums[i] + i)
        return step
# @lc code=end
# %%
# s = Solution()
# s.jump([1, 1, 1, 1, 4])
# %%
