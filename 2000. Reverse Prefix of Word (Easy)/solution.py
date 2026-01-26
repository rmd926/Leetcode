class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        for i in range(len(word)):
            if word[i] == ch:
                return word[:i+1][::-1] + word[i+1:]
                break

        return word

# Runtime: 0 ms Beats 100.00 %
# Memory: 19.51 MB Beats 7.17 %
