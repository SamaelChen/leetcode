#
# @lc app=leetcode.cn id=62 lang=python3
#
# [62] 不同路径
#
# %%
# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        m-=1
        n-=1
        import math
        denominator = math.factorial(m+n)
        numerator = math.factorial(n) * math.factorial(m)
        return int(denominator / numerator)
# @lc code=end


# %%
# s = Solution()
# s.uniquePaths(7, 3)
# %%
