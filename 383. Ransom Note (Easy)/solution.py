from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        lookup = Counter(magazine)

        for char in ransomNote:
            if lookup[char] == 0: # 如果本身不存在於lookup
                return False
            
            lookup[char] -= 1
        return True

# Runtime: 15 ms Beats 78.62 %
# Memory: 19.62 MB Beats 16.86 %
