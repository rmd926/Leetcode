class Solution:
    def fib(self, n: int) -> int:
        MAX = 31 # >= 30即可
        table = [0] * MAX
        table[0], table[1] = 0, 1
        for i in range(2, MAX):
            table[i] = table[i-1] + table[i-2]
        
        return table[n]
