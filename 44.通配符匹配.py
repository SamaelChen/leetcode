#
# @lc app=leetcode.cn id=44 lang=python3
#
# [44] 通配符匹配
#
# %%
# @lc code=start
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s_len, p_len = len(s), len(p)
        i, j, star, i_index = 0, 0, -1, 0
        while i < s_len:
            if j < p_len and (p[j] == '?' or p[j] == s[i]):
                i += 1
                j += 1
            elif j < p_len and p[j] == '*':
                star = j
                j += 1
                i_index = i
            elif star != -1:
                j = star + 1
                i_index += 1
                i = i_index
            else:
                return False

        while j < p_len and p[j] == '*':
            j += 1

        return j == p_len
# @lc code=end
# %%
