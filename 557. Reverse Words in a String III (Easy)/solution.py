class Solution:
    def reverseWords(self, s: str) -> str:
        word = ""
        ans = ""
        for ch in s:
            if ch != " ":
                word += ch
            else:
                ans += word[::-1]
                word = ""
                ans += " "

        if word != " ":
            ans += word[::-1]

        return ans

# Runtime: 19 ms Beats 20.69 %
# Memory: 20.02 MB Beats 9.36 %
