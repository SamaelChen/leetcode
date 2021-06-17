#
# @lc app=leetcode.cn id=862 lang=python3
#
# [862] 和至少为 K 的最短子数组
#
# %%
# @lc code=start
class Solution:
    def shortestSubarray(self, nums, k: int) -> int:
        N = len(nums)
        cdf = [0]
        for num in nums:
            cdf.append(cdf[-1] + num)
        res = N + 1
        que = collections.deque()
        for i, csum in enumerate(cdf):
            while que and csum <= cdf[que[-1]]:
                que.pop()
            while que and csum - cdf[que[0]] >= k:
                res = min(res, i - que.popleft())
            que.append(i)
        return res if res < N + 1 else -1
# @lc code=end
