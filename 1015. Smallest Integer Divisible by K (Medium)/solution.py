class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k % 2 == 0 or k % 5 == 0:
            return -1
        
        r = 0
        for num in range(1, k+1):
            r = (r * 10 + 1) % k
            if r == 0:
                return num
        
        return -1

# Runtime: 15 ms Beats 62.47 %
# Memory: 19.41 MB Beats 30.26 %
