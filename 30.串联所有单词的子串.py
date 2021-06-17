#
# @lc app=leetcode.cn id=30 lang=python3
#
# [30] 串联所有单词的子串
#
# %%
# @lc code=start
class Solution:
    def findSubstring(self, s, words):
        if len(words) == 0 or len(s) == 0:
            return []

        res = []
        for i in range(len(s) - len(words[0]) * len(words) + 1):
            k = i
            tmp = words.copy()
            while tmp:
                if s[k: k+len(words[0])] in tmp:
                    tmp.remove(s[k: k+len(words[0])])
                    k += len(words[0])
                else:
                    break
            if not tmp:
                res.append(i)
        return res
# @lc code=end
