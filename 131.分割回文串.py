#
# @lc app=leetcode.cn id=131 lang=python3
#
# [131] 分割回文串
#
# %%
# @lc code=start
class Solution:
    def partition(self, s: str):
        res = []
        def backTrack(path, string):
            if not string:
                res.append(path)
                return
            for i in range(1, len(string)+1):
                if string[:i] == string[:i][::-1]:
                    backTrack(path+[string[:i]], string[i:])
        backTrack([], s)
        return res

# @lc code=end
# %%
# s = Solution()
# s.partition('aab')
# %%
