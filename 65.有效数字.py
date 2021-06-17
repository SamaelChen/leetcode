#
# @lc app=leetcode.cn id=65 lang=python3
#
# [65] 有效数字
#
# %%
# @lc code=start
class Solution:
    def isNumber(self, s: str) -> bool:
        try:
            float(s)
        except:
            return False
        return True
# @lc code=end

# %%
# s = Solution()
# s.isNumber(" +90.987e3   ")
# %%
