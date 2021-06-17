#
# @lc app=leetcode.cn id=40 lang=python3
#
# [40] 组合总和 II
#
# %%
# @lc code=start
class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()
        def dp(candidates, n, path, res):
            candidates_copy = candidates.copy()
            if n == 0:
                path.sort()
                if path not in res:
                    res.append(path)
                return 0
            if n < 0:
                return -1
            for c in candidates:
                candidates_copy.remove(c)
                subproblem = dp(candidates_copy, n - c, path+[c], res)
                # 子问题无解，跳过
                if subproblem == -1:
                    continue
            if len(candidates) == 0:
                return []
        path = []
        res = []
        dp(candidates, target, path, res)
        return res
# @lc code=end
# %%
%%time
s = Solution()
s.combinationSum2([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 6], 27)
# %%
