#
# @lc app=leetcode.cn id=56 lang=python3
#
# [56] 合并区间
#
# %%
# @lc code=start
class Solution:
    def merge(self, intervals):
        if not intervals:
            return []
        res = []
        intervals.sort()
        for i, interval in enumerate(intervals):
            left, right = interval
            if res and left <= res[-1][1]:
                res[-1][1] = max(res[-1][1], right)
            else:
                res.append(interval)
        return res

# @lc code=end