class Solution:
    def climbStairs(self, n: int) -> int:
        table = [0] * 46
        table[0], table[1] = 1, 1
        ans = 0
        for i in range(2, len(table)):
            table[i] = table[i-1] + table[i-2]
        
        return table[n]
