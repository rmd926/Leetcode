class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        left = money - (prices[0] + prices[1])

        if left < 0:
            return money
        else:
            return left

# Runtime: 0 ms Beats 100.00 %
# Memory: 19.53 MB Beats 12.47 %
