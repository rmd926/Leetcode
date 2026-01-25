class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        for i in range(2, n-1):
            temp = n
            digit = ""
            while temp > 0:
                r = temp % i
                digit = str(r) + digit
                temp //= i
            if digit != digit[::-1]:
                return False
        return True

# Runtime: 0 ms Beats 100.00 %
# Memory: 19.21 MB Beats 34.06 %
