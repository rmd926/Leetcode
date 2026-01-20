class Solution:
    def pivotInteger(self, n: int) -> int:
        total = n * (n+1) // 2
        x = int(total ** 0.5)
        if x*x == total:
            return x
        else:
            return -1

# Runtime: 0 ms Beats 100.00 %
# Memory: 19.29 MB Beats 17.92 %
