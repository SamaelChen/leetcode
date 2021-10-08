#
# @lc app=leetcode.cn id=187 lang=python3
#
# [187] 重复的DNA序列
#
# %%
# @lc code=start
class Solution:
    def findRepeatedDnaSequences(self, s: str):
        cnt = {}
        res = []
        for i in range(len(s) - 9):
            if s[i: i+10] not in cnt:
                cnt[s[i: i+10]] = 1
            else:
                cnt[s[i: i+10]] += 1
            if cnt[s[i: i+10]] >= 2:
                res.append(s[i: i+10])
        return list(set(res))


# @lc code=end
# %%
