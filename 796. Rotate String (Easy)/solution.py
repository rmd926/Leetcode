class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        n = len(s)
        status = False
        temp = ""
        for i in range(n):
            temp = s[i:] + s[:i]
            if temp != goal:
                continue
            else:
                status = True
                break
        
        return status

# Runtime: 0 ms Beats 100.00 %
# Memory: 19.15 MB Beats 86.04 %
