#
# @lc app=leetcode.cn id=39 lang=python3
#
# [39] 组合总和
#
# %%
# @lc code=start


class Solution:
    def combinationSum(self, candidates, target):
        def dp(n, path, res):
            if n == 0:
                path.sort()
                if path not in res:
                    res.append(path)
                return 0
            if n < 0:
                return -1
            for c in candidates:
                subproblem = dp(n - c, path+[c], res)
                # 子问题无解，跳过
                if subproblem == -1:
                    continue
            if len(candidates) == 0:
                return []
        path = []
        res = []
        dp(target, path, res)
        return res


# @lc code=end