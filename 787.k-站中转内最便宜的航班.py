#
# @lc app=leetcode.cn id=787 lang=python3
#
# [787] K 站中转内最便宜的航班
#
# %%
# @lc code=start
import collections
import heapq
class Solution:
    def findCheapestPrice(self, n: int, flights, src: int, dst: int, k: int) -> int:
        graph_neighbor = collections.defaultdict(list)
        for s, e, c in flights:
            graph_neighbor[s].append([e, c])
        prices = {}
        steps = {}
        heap = [(0, 0, src)]
        while len(heap) > 0:
            print(heap)
            price, step, node = heapq.heappop(heap)
            if node == dst:
                return price
            if node not in prices:
                prices[node] = price
            steps[node] = step
            if step <= k:
                step += 1
                for n, p in graph_neighbor[node]:
                    if n not in prices or step < steps[n]:
                        heapq.heappush(heap, (p + price, step, n))
        return -1
# @lc code=end

# %%
s = Solution()
s.findCheapestPrice(n=3, flights=[[0, 1, 100], [1, 2, 100], [0, 2, 500]],
                    src=0, dst=2, k=1)
# %%
