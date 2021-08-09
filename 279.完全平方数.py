#
# @lc app=leetcode.cn id=279 lang=python3
#
# [279] 完全平方数
#
# %%
# @lc code=start
class Solution:
    def numSquares(self, n: int) -> int:
        last = int(n ** 0.5)
        dp = [0] + [float('inf') for _ in range(n)]
        for i in range(1, last+1):
            curr = i * i
            for j in range(curr, n+1):
                dp[j] = min(dp[j], dp[j-curr]+1)
        return dp[-1]
# @lc code=end
# %%
# s = Solution()
# s.numSquares(13)
# %%
