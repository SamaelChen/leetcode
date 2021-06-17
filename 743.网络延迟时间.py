#
# @lc app=leetcode.cn id=743 lang=python3
#
# [743] 网络延迟时间
#
# %%
# @lc code=start
import collections
import heapq


class Solution:
    def networkDelayTime(self, times, n: int, k: int) -> int:
        graph_neighbor = collections.defaultdict(list)
        for s, e, t in times:
            graph_neighbor[s].append((e, t))
        visted = {}
        heap = [(0, k)]
        while heap:
            delay, node = heapq.heappop(heap)
            if node not in visted:
                visted[node] = delay
                for n, d in graph_neighbor[node]:
                    if n not in visted:
                        heapq.heappush(heap, (d+delay, n))
        return max(visted.values()) if len(visted) == n else -1
# @lc code=end
# %%
