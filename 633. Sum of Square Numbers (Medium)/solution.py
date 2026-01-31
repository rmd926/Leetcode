class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        for i in range(int(c**0.5)+1):
            rest = c - i**2
            b = int(rest ** 0.5)
            if b * b == rest:
                return True

        return False

# Runtime: 91 ms Beats 29.52 %
# Memory: 19.29 MB Beats 42.74 %
