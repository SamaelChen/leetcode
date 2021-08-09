#
# @lc app=leetcode.cn id=322 lang=python3
#
# [322] 零钱兑换
#
# %%
# @lc code=start
class Solution:
    def coinChangeBackTrack(self, coins, amount: int) -> int:
        memo = {0:0}
        def backTrack(amount):
            if amount in memo:
                return memo[amount]
            res = float('inf')
            for coin in coins:
                if amount >= coin:
                    res = min(res, backTrack(amount-coin)+1)
            memo[amount] = res
            return res
        cnt = backTrack(amount)
        return cnt if cnt != float('inf') else -1

    def coinChange(self, coins, amount):
        dp = [float('inf') for _ in range(amount+1)]
        dp[0] = 0
        for i in range(1, amount+1):
            for coin in coins:
                if i >= coin:
                    dp[i] = min(dp[i-coin]+1, dp[i])
        return dp[amount] if dp[amount] != float('inf') else -1
# @lc code=end
# %%
# s = Solution()
# s.coinChange([2, 10, 3], 11)
# %%
