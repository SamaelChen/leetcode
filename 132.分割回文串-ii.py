#
# @lc app=leetcode.cn id=132 lang=python3
#
# [132] 分割回文串 II
#
# %%
# @lc code=start
class Solution:
    def minCutBrutal(self, s: str) -> int:
        if len(s) == 1:
            return 0
        res = []
        def backTrack(s, path):
            if not s:
                res.append(len(path) - 1)
                return
            for i in range(1, len(s)+1):
                if s[:i] == s[:i][::-1]:
                    backTrack(s[i:], path+[s[:i]])
        backTrack(s, [])
        return min(res)

    def minCut(self, s):
        if len(s) == 1:
            return 0
        dp = [x for x in range(len(s)+1)]
        for i in range(1, len(s)+1):
            if s[:i] == s[:i][::-1]:
                dp[i] = 0
            else:
                for j in range(i):
                    if s[j:i] == s[j:i][::-1]:
                        dp[i] = min(dp[j]+1, dp[i])
        return dp[-1]


# @lc code=end

# %%
# s = Solution()
# s.minCut('ababababababababababababcbabababababababababababa')
# s.minCut('coder')
# %%
