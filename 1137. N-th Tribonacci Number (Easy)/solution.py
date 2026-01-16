class Solution:
    def tribonacci(self, n: int) -> int:
        MAX = 38
        table = [0] * MAX
        table[0], table[1], table[2] = 0, 1, 1

        for i in range(3, MAX):
            table[i] = table[i-1] + table[i-2] + table[i-3]

        return table[n]

# Runtime: 0 ms Beats 100.00%
# Memory: 19.21 MB Beats 13.97%
