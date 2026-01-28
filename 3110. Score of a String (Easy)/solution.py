class Solution:
    def scoreOfString(self, s: str) -> int:
        ans = 0
        # s = list(s)
        for i in range(1, len(s)):
            ans += abs(ord(s[i]) - ord(s[i-1]))
        return ans

# Runtime: 0 ms Beats 100.00 %
# Memory: 19.23 MB Beats 31.53 %
