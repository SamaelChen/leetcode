#
# @lc app=leetcode.cn id=1383 lang=python3
#
# [1383] 最大的团队表现值
#
# %%
# @lc code=start
from itertools import combinations
import heapq
class Solution:
    def maxPerformanceBrutal(self, n: int, speed, efficiency, k: int) -> int:
        max_performance = 0
        for n_select in range(1, k+1):
            for c in combinations(range(n), n_select):
                s, e = 0, float('inf')
                for elem in c:
                    s += speed[elem]
                    e = min(e, efficiency[elem])
                max_performance = max(max_performance, s * e)
        return max_performance % (10e9 + 7)
    
    def maxPerformance(self, n: int, speed, efficiency, k: int) -> int:
        people = sorted(zip(speed, efficiency), key=lambda x: x[1], reverse=True)
        max_performance, sum_s = 0, 0
        min_heap = []
        for s, e in people:
            if len(min_heap) < k:
                sum_s += s
                heapq.heappush(min_heap, s)
            elif s > min_heap[0]:
                sum_s += s - heapq.heappushpop(min_heap, s)
            max_performance = max(max_performance, sum_s * e)
        return int(max_performance % (10 ** 9 + 7))
# @lc code=end
# %%
