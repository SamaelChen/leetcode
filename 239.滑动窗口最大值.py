#
# @lc app=leetcode.cn id=239 lang=python3
#
# [239] 滑动窗口最大值
#
# %%
# @lc code=start
class Solution:
    def maxSlidingWindowBrutal(self, nums, k: int):
        N = len(nums)
        if N * k == 0:
            return []
        if k == 1:
            return nums
        res = []
        for i in range(N-k+1):
            res.append(max(nums[i: i+k]))
        return res
    def maxSlidingWindow(self, nums, k):
        N = len(nums)
        if N * k == 0:
            return []
        if k == 1:
            return nums
        
        que = []
        res = []
        for i in range(N):
            if que and que[0] == i - k:
                que = que[1:]
            while que and nums[i] >= nums[que[-1]]:
                que.pop()
            que.append(i)
            if i >= k-1:
                res.append(nums[que[0]])
        return res
# class Solution:
#     def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
#         n = len(nums)
#         q = collections.deque()
#         for i in range(k):
#             while q and nums[i] >= nums[q[-1]]:
#                 q.pop()
#             q.append(i)

#         ans = [nums[q[0]]]
#         for i in range(k, n):
#             while q and nums[i] >= nums[q[-1]]:
#                 q.pop()
#             q.append(i)
#             while q[0] <= i - k:
#                 q.popleft()
#             ans.append(nums[q[0]])

#         return ans

# @lc code=end
# %%
s = Solution()
s.maxSlidingWindow([1, 3, -1], 3)

# %%
