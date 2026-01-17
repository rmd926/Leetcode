class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        
        for ch in s:
            if ch == "*":
                stack.pop()
            else:
                stack.append(ch)
        return "".join(stack)

# Runtime: 89 ms Beats 83.68 %
# Memory: 20.56 MB Beats 14.56 %
