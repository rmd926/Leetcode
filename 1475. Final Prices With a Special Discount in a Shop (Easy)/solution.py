from typing import List

class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        result = prices.copy()
        stack = []                  # 存「還沒找到折扣的商品 index」

        for i in range(len(prices)):
            current_price = prices[i]

            # 如果 current_price 可以當作前面某個商品的折扣（<= 那個商品價格）
            while stack and current_price <= prices[stack[-1]]:
                j = stack.pop()                 # j 這個商品找到折扣了
                result[j] = prices[j] - current_price

            # i 這個商品先放進去，等待未來右邊的折扣
            stack.append(i)

        return result

# Runtime: 1 ms Beats 64.72 %
# Memory: 19.48 MB Beats 22.03 %
