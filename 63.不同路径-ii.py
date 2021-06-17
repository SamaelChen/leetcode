#
# @lc app=leetcode.cn id=63 lang=python3
#
# [63] 不同路径 II
#
# %%
# @lc code=start
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        memo = {}
        m = len(obstacleGrid) - 1
        n = len(obstacleGrid[0]) - 1
        if obstacleGrid[0][0] == 1 or obstacleGrid[m][n] == 1:
            return 0
        def dp(i, j):
            if i == 0 and j == 0:
                return 1
            if i < 0 or j < 0 or obstacleGrid[i][j] == 1:
                return 0
            if str(i)+','+str(j) in memo:
                pass
            else:
                memo[str(i)+','+str(j)] = dp(i-1, j) + dp(i, j-1)
            return memo[str(i)+','+str(j)]
        res = dp(m, n)
        return res

# class Solution(object):
#     def uniquePathsWithObstacles(self, obstacleGrid):
#         r, l = len(obstacleGrid), len(obstacleGrid[0])
#         for i in range(r):
#             for j in range(l):
#                 if obstacleGrid[i][j] != 1:
#                     if i == 0 and j == 0:
#                         obstacleGrid[i][j] = 1
#                     elif i == 0 and j != 0:
#                         obstacleGrid[i][j] = obstacleGrid[i][j-1]
#                     elif i != 0 and j == 0:
#                         obstacleGrid[i][j] = obstacleGrid[i - 1][j]
#                     else:
#                         obstacleGrid[i][j] = obstacleGrid[i -
#                                                           1][j] + obstacleGrid[i][j - 1]
#                 else:
#                     obstacleGrid[i][j] = 0
#         return obstacleGrid[r - 1][l - 1]
# @lc code=end
# %%
# %%time
# s = Solution()
# s.uniquePathsWithObstacles([[0,0,0,0,0,1,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,1,0,0,0,0,1,0,1,0,1,0,0],[1,0,0,0,0,0,1,0,0,0,0,0,1,0,1,1,0,1],[0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0],[0,0,0,0,0,1,0,0,0,0,1,1,0,1,0,0,0,0],[1,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,1,0],[0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0],[0,0,1,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0],[0,1,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0],[0,0,1,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1],[0,1,0,1,0,1,0,0,0,0,0,0,0,1,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1],[1,0,1,1,0,0,0,0,0,0,1,0,1,0,0,0,1,0],[0,0,0,1,0,0,0,0,1,1,1,0,0,1,0,1,1,0],[0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,1,1,0,0,1,0,0,0,0,0,0,0,1,1,0,0,0],[0,0,0,0,0,0,1,0,1,0,0,1,0,1,1,1,0,0],[0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,1,1],[0,1,0,0,0,0,0,0,0,0,1,0,1,0,1,0,1,0],[1,0,0,1,0,1,0,0,1,0,0,0,0,0,0,0,0,0],[0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0],[0,1,0,0,0,0,0,1,0,0,0,0,0,0,1,1,1,0],[1,0,1,0,1,0,0,0,0,0,0,1,1,0,0,0,0,1],[1,0,0,0,0,0,1,1,0,0,0,1,0,0,0,0,0,0]])
# %%
