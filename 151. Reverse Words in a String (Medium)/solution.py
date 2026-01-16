class Solution:
    def reverseWords(self, s: str) -> str:
        if s == "":
            return ""
        words = s.split()
        return " ".join(words[::-1])
