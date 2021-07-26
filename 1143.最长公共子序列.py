#
# @lc app=leetcode.cn id=1143 lang=python3
#
# [1143] 最长公共子序列
#

# @lc code=start
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) == 0 or len(text2) == 0:
            return 0
        m, n = len(text1), len(text2)
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if text1[i] == text2[j]:
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
                else:
                    if i == 0 and j != 0:
                        dp[i][j] = dp[i][j-1]
                    elif i != 0 and j == 0:
                        dp[i][j] = dp[i-1][j]
                    else:
                        dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[m-1][n-1]
# @lc code=end

