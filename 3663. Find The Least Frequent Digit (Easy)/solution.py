class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:
        lookup = {}
        for ch in str(n):
            if ch not in lookup:
                lookup[ch] = 1
            else:
                lookup[ch] += 1

        for key, value in sorted(lookup.items(), key=lambda x: (x[1], x[0])):
            return int(key)

# Runtime: 1 ms Beats 53.79 %
# Memory: 19.40 MB Beats 47.22 %
