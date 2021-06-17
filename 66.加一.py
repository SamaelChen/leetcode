#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#
# %%
# @lc code=start
class Solution:
    def plusOne(self, digits):
        # tmp = int(''.join([str(x) for x in digits]))
        # tmp += 1
        # return [int(x) for x in str(tmp)]
        idx = len(digits) - 1
        while digits[idx] == 9:
            digits[idx] = 0
            idx -= 1
        if idx < 0:
            return [1] + digits
        else:
            digits[idx] += 1
            return digits

# @lc code=end

# %%
# %%time
# s = Solution()
# s.plusOne([0, 0, 0])
# %%
