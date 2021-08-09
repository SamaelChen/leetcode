#
# @lc app=leetcode.cn id=518 lang=python3
#
# [518] 零钱兑换 II
#
# %%
# @lc code=start
class Solution:
    def changeBrutal(self, amount: int, coins) -> int:
        res = []
        def backTrack(amount, path):
            if amount == 0:
                path.sort()
                if path not in res:
                    res.append(path[:])
            if amount < 0:
                return
            for coin in coins:
                path.append(coin)
                backTrack(amount-coin, path)
                path.pop()
        backTrack(amount, [])
        return len(res)

    def change(self, amount, coins):
        if amount == 0:
            return 1
        m, n = len(coins) + 1, amount + 1
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                if j < coins[i-1]:
                    dp[i][j] = dp[i-1][j]
                elif j == coins[i-1]:
                    dp[i][j] = dp[i-1][j] + 1
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-coins[i-1]]
        return dp[m-1][n-1]
# @lc code=end
