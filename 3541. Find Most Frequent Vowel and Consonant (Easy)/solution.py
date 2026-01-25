class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels = "aeiou"
        count = 0
        lookup_v = {}
        lookup_c = {}

        for char in s:
            if char in vowels and char not in lookup_v:
                lookup_v[char] = 1
            elif char in vowels and char in lookup_v:
                lookup_v[char] += 1
            elif char not in vowels and char not in lookup_c:
                lookup_c[char] = 1
            elif char not in vowels and char in lookup_c:
                lookup_c[char] += 1
        
        if lookup_v:
            v_max = max(lookup_v.values())
        else:
            v_max = 0
        if lookup_c:
            c_max = max(lookup_c.values())
        else:
            c_max = 0
        return v_max + c_max

# Runtime: 6 ms Beats 16.62 %
# Memory: 19.40 MB Beats 24.29 %
