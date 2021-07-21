#
# @lc app=leetcode.cn id=55 lang=python3
#
# [55] 跳跃游戏
#
# %%
# @lc code=start
class Solution:
    def canJumpPlagiarize(self, nums):
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
    
    def canJump(self, nums):
        if len(nums) == 1:
            return True
        max_position = 0
        dp = [False for _ in range(len(nums))]
        dp[0] = True if nums[0] != 0 else False
        for i in range(1, len(nums)):
            max_position = max(max_position, nums[i-1] + i-1)
            dp[i] = dp[i-1] and max_position >= i
        return dp[-1]
# @lc code=end
# %%
# s = Solution()
# s.canJump([3, 2, 1, 0, 4])
# %%
