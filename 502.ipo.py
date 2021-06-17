#
# @lc app=leetcode.cn id=502 lang=python3
#
# [502] IPO
#
# %%
# @lc code=start
import heapq
import collections
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits, capital) -> int:
        if w > max(capital):
            return w + sum(heapq.nlargest(k, profits))
        n = len(profits)
        projects = sorted(zip(profits, capital), key=lambda x: (x[1], -x[0]))
        projects = collections.deque(projects)
        available = []
        while k > 0:
            while projects and projects[0][1] <= w:
                heapq.heappush(available, -projects.popleft()[0])
            if available:
                w -= heapq.heappop(available)
            else:
                break
            k -= 1
        return w

# @lc code=end
# %%
# s = Solution()
# s.findMaximizedCapital(2, 0, [1, 2, 3], [0, 1, 1])
# %%
