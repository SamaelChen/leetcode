#
# @lc app=leetcode.cn id=1529 lang=python3
#
# [1529] 灯泡开关 IV
#
# %%
# @lc code=start
class Solution:
    def minFlips(self, target: str) -> int:
        cnt = 0
        prev = '0'
        for curr in target:
            if curr != prev:
                cnt += 1
                prev = curr
        return cnt
# @lc code=end

# %%
