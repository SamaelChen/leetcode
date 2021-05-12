#
# @lc app=leetcode.cn id=150 lang=python3
#
# [150] 逆波兰表达式求值
#
# %%
# @lc code=start
class Solution:
    def evalRPN(self, tokens) -> int:
        stack = []
        for item in tokens:
            if item not in ['+', '-', '*', '/']:
                stack.append(int(item))
            else:
                a = stack.pop()
                b = stack.pop()
                print(a, b)
                if item == '+':
                    stack.append(b + a)
                elif item == '-':
                    stack.append(b - a)
                elif item == '*':
                    stack.append(b * a)
                else:
                    if a * b < 0:
                        stack.append(-(abs(b) // abs(a)))
                    else:
                        stack.append(b // a)
        return stack.pop()
# @lc code=end