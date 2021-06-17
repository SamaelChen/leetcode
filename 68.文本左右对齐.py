#
# @lc app=leetcode.cn id=68 lang=python3
#
# [68] 文本左右对齐
#

# @lc code=start
class Solution:
    def fullJustify(self, words, maxWidth):
        lens = [len(x) for x in words]
        if maxWidth < max(lens):
            return
        res = []
        elements_len = 0
        for i in lens:
            if element_len + i > maxWidth:
                res
# @lc code=end

# %%
s = Solution()
s.fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16)