class Solution:
    def firstUniqChar(self, s: str) -> int:
        lookup = {}

        for ch in s:
            if ch not in lookup:
                lookup[ch] = 1
            else:
                lookup[ch] += 1

        for i in range(len(s)):
            if lookup[s[i]] == 1:
                return i

        return -1

# Runtime: 71 ms Beats 59.41 %
# Memory: 19.52 MB Beats 88.86 %
