class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        temp = 0
        cur = x
        while cur >= 10:
            temp += cur % 10
            cur //= 10
        temp += cur
        
        if x % temp == 0:
            return temp
        else:
            return -1

# Runtime: 0 ms Beats 100.00 %
# Memory: 19.34 MB Beats 16.39 %
