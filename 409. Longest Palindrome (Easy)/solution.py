class Solution:
    def longestPalindrome(self, s: str) -> int:
        lookup = {}
        for ch in s:
            if ch not in lookup:
                lookup[ch] = 1
            else:
                lookup[ch] += 1

        ans = 0
        temp = []
        for key, value in lookup.items():
            if value % 2 == 0:
                ans += value
            else:
                temp.append(value)

        if temp:
            ans += sum(temp) - len(temp) + 1
        
        return ans

# Runtime: 2 ms Beats 53.97 %
# Memory: 19.23 MB Beats 66.89 %
