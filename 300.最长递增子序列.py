#
# @lc app=leetcode.cn id=300 lang=python3
#
# [300] 最长递增子序列
#
# %%
# @lc code=start
class Solution:
    def lengthOfLISDP(self, nums):
        if len(nums) == 1:
            return 1
        dp = [1 for _ in range(len(nums))]
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)


    def lengthOfLIS(self, nums) -> int:
        if len(nums) == 1:
            return 1
        res = []
        for n in nums:
            if not res or n > res[-1]:
                res.append(n)
            else:
                l, r = 0, len(res) - 1
                loc = r
                while l <= r:
                    mid = (l + r) // 2
                    if n > res[mid]:
                        l = mid + 1
                    else:
                        loc = mid
                        r = mid - 1
                res[loc] = n
        return len(res)

    def LIS(self, nums):
        length = self.lengthOfLIS(nums)
        res = []
        def backTrack(nums, path):
            if len(path) == length:
                res.append(path[:])
                return
            for i, n in enumerate(nums):
                if not path or n > path[-1]:
                    path.append(n)
                    backTrack(nums[(i+1):], path)
                    path.pop()
        backTrack(nums, [])
        return res
# @lc code=end
# %%
# s = Solution()
# s.LIS([10, 9, 2, 5, 3, 7, 101, 18])
# %%
