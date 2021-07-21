#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#
# %%
# @lc code=start
class Solution:
    def __init__(self) -> None:
        self.memo = {1: 1, 2: 2}

    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        if n in self.memo:
            return self.memo[n]
        else:
            self.memo[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return self.memo[n]
# @lc code=end


# %%
# s = Solution()
# s.climbStairs(44)
# %%
