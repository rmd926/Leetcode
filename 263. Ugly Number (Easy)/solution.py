class Solution:
    def isUgly(self, n: int) -> bool:
        prime_factor = [2, 3, 5]
        if n <= 0:
            return False
        
        for p in prime_factor:
            while n % p == 0:
                n //= p
        
        return n == 1

# Runtime: 0 ms Beats 100.00 %
# Memory: 19.63 MB Beats 5.52 %
