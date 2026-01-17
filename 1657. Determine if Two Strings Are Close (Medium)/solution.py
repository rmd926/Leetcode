from collections import Counter
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        
        word1_lookup = Counter(word1)
        word2_lookup = Counter(word2)

        return word1_lookup.keys() == word2_lookup.keys() and sorted(word1_lookup.values()) == sorted(word2_lookup.values())

# Runtime: 79 ms Beats 90.54 %
# Memory: 20.92 MB Beats 6.96 %
