class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        lookup = {}
        for ch in str(n):
            if ch not in lookup:
                lookup[ch] = 1
            else:
                lookup[ch] += 1
        
        ans = 0
        for key, value in lookup.items():
            ans += int(key) * value
        
        return ans

# Runtime: 0 ms Beats 100.00 %
# Memory: 19.31 MB Beats 27.63 %
