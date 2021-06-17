#
# @lc app=leetcode.cn id=28 lang=python3
#
# [28] 实现 strStr()
#
# %%
# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0
        elif len(haystack) == 0:
            return -1
        elif haystack == needle:
            return 0
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i: (i+len(needle))] == needle:
                return i
        return -1
# @lc code=end
