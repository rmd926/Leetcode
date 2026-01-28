class Solution:
    def maxProduct(self, n: int) -> int:
        temp = []
        for num in str(n):
            temp.append(int(num))
            temp.sort()

        return temp[-1] * temp[-2]

# Runtime: 0 ms Beats 100.00 %
# Memory: 19.33 MB Beats 26.75 %
