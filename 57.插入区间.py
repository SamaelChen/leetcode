#
# @lc app=leetcode.cn id=57 lang=python3
#
# [57] 插入区间
#
# %%
# @lc code=start
class Solution:
    def insert(self, intervals, newInterval):
        if not newInterval:
            return intervals
        intervals.append(newInterval)
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
# %%
