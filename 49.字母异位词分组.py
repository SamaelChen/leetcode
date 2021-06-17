#
# @lc app=leetcode.cn id=49 lang=python3
#
# [49] 字母异位词分组
#
# %%
# @lc code=start
class Solution:
    def groupAnagrams(self, strs):
        groups = []
        ch_cnt = []
        res = {}
        for word in strs:
            word_ch = set(word)
            ch_dic = {}
            for x in word_ch:
                ch_dic[x] = word.count(x)
            if (word_ch not in groups) or (ch_dic not in ch_cnt):
                groups.append(word_ch)
                ch_cnt.append(ch_dic)
                idx = ch_cnt.index(ch_dic)
                res[idx] = []
                res[idx].append(word)
            else:
                idx = ch_cnt.index(ch_dic)
                res[idx].append(word)
        return list(res.values())

# @lc code=end
# %%
