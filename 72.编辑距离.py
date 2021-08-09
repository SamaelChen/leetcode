#
# @lc app=leetcode.cn id=72 lang=python3
#
# [72] 编辑距离
#
# %%
# @lc code=start
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if len(word1) == 0:
            return len(word2)
        elif len(word2) == 0:
            return len(word1)
        m, n = len(word1)+1, len(word2)+1
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    dp[i][j] = max(i, j)
                else:
                    if word1[i-1] == word2[j-1]:
                        dp[i][j] = min(dp[i-1][j-1], dp[i-1][j]+1, dp[i][j-1]+1)
                    else:
                        dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
        return dp[m-1][n-1]
# @lc code=end
# %%
# s = Solution()
# s.minDistance('horse', 'ros')
# %%
