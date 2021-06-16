#
# @lc app=leetcode.cn id=338 lang=python3
#
# [338] 比特位计数
#
# %%
# @lc code=start
class Solution:
    def countBits(self, n: int):
        res = []
        for i in range(n+1):
            cnt = 0
            tmp = bin(i)
            for c in tmp:
                if c == '1':
                    cnt += 1
            res.append(cnt)
        return res
# @lc code=end
# %%
