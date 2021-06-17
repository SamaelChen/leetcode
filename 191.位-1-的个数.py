#
# @lc app=leetcode.cn id=191 lang=python3
#
# [191] 位1的个数
#
# %%
# @lc code=start
class Solution:
    def hammingWeight(self, n: int) -> int:
        n = bin(n)
        res = 0
        for i in n:
            if i == '1':
                res += 1
        return res
# @lc code=end
