class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = "aeiou"
        # temp = s[:k]
        count = 0
        for char in s[:k]:
            if char in vowels:
                count += 1

        max_count = count
        for i in range(k, len(s)):
            if s[i] in vowels and s[i-k] not in vowels:
                count += 1
            elif s[i] in vowels and s[i-k] in vowels:
                count = count
            elif s[i] not in vowels and s[i-k] in vowels:
                count -= 1
            else:
                count = count
                
            max_count = max(max_count, count)
        
        return max_count
# Runtime: 59 ms Beats 82.18%
# Memory: 19.88 MB Beats: 16.13%
