#
# @lc app=leetcode.cn id=29 lang=python3
#
# [29] 两数相除
#
# %%
# @lc code=start
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        res = 0
        if divisor == 0:
            return None
        if (divisor > 0 and dividend > 0) or (dividend < 0 and divisor < 0):
            flag = 1
        else:
            flag = -1
        dividend = abs(dividend)
        divisor = abs(divisor)
        while divisor <= dividend:
            tmp_divisor, count = divisor, 1
            while tmp_divisor <= dividend:
                dividend -= tmp_divisor
                res += count
                count <<= 1
                tmp_divisor <<= 1
        res = res * flag
        if res < - 2 ** 31:
            return - 2 ** 31
        elif res > 2 ** 31 - 1:
            return 2 ** 31 - 1
        return res


# @lc code=end
