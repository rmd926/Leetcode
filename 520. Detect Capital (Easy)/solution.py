class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        status = False
        if word == word.upper() or word == word.lower():
            status = True
        else:
            if word[0] == word[0].upper() and word[1:] == word[1:].lower():
                status = True
        
        return status

# Runtime: 0 ms Beats 100.00 %
# Memory: 19.40 MB Beats 23.31 %
