class Solution:
    def trailingZeroes(self, n: int) -> int:
        # 只要計算有多少5這個質因數，因為需要考慮完全平方數，所以用recursive去做
        if n == 0:
            return 0
        else:
            return n // 5 + self.trailingZeroes(n//5)

# Runtime: 0 ms Beats 100.00 %
# Memory: 19.36 MB Beats 46.97 %
