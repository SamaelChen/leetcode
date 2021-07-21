#
# @lc app=leetcode.cn id=638 lang=python3
#
# [638] 大礼包
#
# %%
# @lc code=start

class Solution:
    def shoppingOffers(self, price, special, needs) -> int:
        memo = {}
        # 给定物品价格，大礼包分布和需要的物品数量，返回最少花费

        def shop(price, special, needs):
            if not any(needs):
                return 0
            if str(needs) in memo:
                return memo[str(needs)]
            # 不选择礼包
            cost = sum([price[i] * needs[i] for i in range(len(needs))])
            # 选择大礼包
            for sp in special:
                need = []
                for i in range(len(needs)):
                    if needs[i] - sp[i] < 0:
                        break
                    else:
                        need.append(needs[i] - sp[i])
                if len(needs) == len(need):
                    cost = min(cost, sp[-1] + shop(price, special, need))
            memo[str(needs)] = cost
            return cost
        return shop(price, special, needs)
# @lc code=end
# %%
