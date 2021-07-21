#
# @lc app=leetcode.cn id=416 lang=python3
#
# [416] 分割等和子集
#
# %%
# @lc code=start
class Solution:
    def canPartition(self, nums) -> bool:
        if sum(nums) % 2 != 0 or len(nums) == 1 or max(nums) > sum(nums) / 2:
            return False
        target = sum(nums) // 2
        dp = [[False for _ in range(target+1)] for _ in range(len(nums))]
        for i in range(len(nums)):
            dp[i][0] = True
        dp[0][nums[0]] = True
        for i in range(1, len(nums)):
            for j in range(target+1):
                if j < i:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i]]
        return dp[-1][-1]
# @lc code=end
# %%
