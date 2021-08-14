#
# @lc app=leetcode.cn id=1449 lang=python3
#
# [1449] 数位成本和为目标值的最大数字
#
# %%
# @lc code=start
class Solution:
    def largestNumber(self, cost, target: int) -> str:
        dp = [[float('-inf') for _ in range(target+1)] for _ in range(10)]
        dp[0][0] = 0
        addr = [[0 for _ in range(target+1)] for _ in range(10)]
        for i in range(1, 10):
            for j in range(target+1):
                if j < cost[i-1]:
                    dp[i][j] = dp[i-1][j]
                    addr[i][j] = j
                else:
                    if dp[i-1][j] <= dp[i][j-cost[i-1]] + 1:
                        dp[i][j] = dp[i][j-cost[i-1]] + 1
                        addr[i][j] = j - cost[i-1]
                    else:
                        dp[i][j] = dp[i-1][j]
                        addr[i][j] = j
        if dp[9][target] < 0:
            return '0'
        res = []
        i, j = 9, target
        while i > 0:
            if j == addr[i][j]:
                i -= 1
            else:
                res.append(str(i))
                j = addr[i][j]
        return ''.join(res)


# @lc code=end
# %%
# s = Solution()
# s.largestNumber(cost=[4, 3, 2, 5, 6, 7, 2, 5, 5], target=9)

# %%
