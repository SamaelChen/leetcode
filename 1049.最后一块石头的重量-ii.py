#
# @lc app=leetcode.cn id=1049 lang=python3
#
# [1049] 最后一块石头的重量 II
#
# %%
# @lc code=start
class Solution:
    def lastStoneWeightIIBrutal(self, stones) -> int:
        res = float('inf')
        n = len(stones)
        for i in range(2 ** n):
            s = 0
            choice = bin(i).replace('0b', '').zfill(n)
            for c, stone in zip(choice, stones):
                s += (stone if c == '1' else -stone)
            if s > 0:
                res = min(res, s)
        return res

    def lastStoneWeightII(self, stones):
        total = sum(stones)
        half = total // 2
        nums = len(stones) + 1
        dp = [[0 for _ in range(half + 1)] for _ in range(nums)]
        for i in range(1, nums):
            for j in range(1, half+1):
                if j < stones[i-1]:
                    dp[i][j] = dp[i-1][j]
                elif j == stones[i-1]:
                    dp[i][j] = stones[i-1]
                else:
                    dp[i][j] = max(dp[i-1][j-stones[i-1]]+stones[i-1], dp[i-1][j])
        return total - 2 * dp[nums-1][half]
# @lc code=end
# %%
# s = Solution()
# s.lastStoneWeightIIBrutal([31, 26, 33, 21, 40])
# s.lastStoneWeightII([1, 2])
# %%
