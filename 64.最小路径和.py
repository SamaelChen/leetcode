#
# @lc app=leetcode.cn id=64 lang=python3
#
# [64] 最小路径和
#
# %%
# @lc code=start
class Solution:
    def minPathSum(self, grid):
        m = len(grid) - 1
        n = len(grid[0]) - 1
        memo = {}
        def dp(i, j):
            if i == 0 and j == 0:
                return grid[i][j]
            if i < 0 or j < 0:
                return 2 ** 32
            if str(i)+','+str(j) in memo:
                pass
            else:
                memo[str(i)+','+str(j)] = min(dp(i-1, j), dp(i, j-1)) + grid[i][j]
            return memo[str(i)+','+str(j)]
        res = dp(m, n)
        return res
# @lc code=end

# %%
# s = Solution()
# s.minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]])

# %%
