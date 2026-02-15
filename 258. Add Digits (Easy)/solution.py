class Solution:
    def addDigits(self, num: int) -> int:
        while num > 9:
            temp = num
            remain = temp % 10
            temp //= 10
            num = temp + remain
        
        return num

# Runtime: 0 ms Beats 100.00 %
# Memory: 19.34 MB Beats 39.83 %
