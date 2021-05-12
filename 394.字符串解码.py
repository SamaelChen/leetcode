#
# @lc app=leetcode.cn id=394 lang=python3
#
# [394] 字符串解码
#
# %%
# @lc code=start
class Solution:
    def decodeString(self, s: str) -> str:
        import string
        times = []
        eles = ['']
        num = 0
        for item in s:
            if item in string.digits:
                num = num * 10 + int(item)
            elif item == '[':
                times.append(num)
                eles.append('')
                num = 0
            elif item == ']':
                curr_str = eles.pop()
                eles[-1] += curr_str * times.pop()
            else:
                eles[-1] += item
        return eles[0]
            
# @lc code=end
# %%
