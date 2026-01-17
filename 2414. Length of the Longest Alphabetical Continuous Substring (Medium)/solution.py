class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        temp = 1 # 初始連續長度
        ans = temp
        if len(s) == 1:
            return 1
        
        for i in range(1, len(s)):
            if ord(s[i]) - ord(s[i-1]) == 1:
                temp += 1
                ans = max(ans, temp)
            else:
                temp = 1 # 如果中斷時，就把temp改寫成1
        
        return ans
# Runtime: 121 ms Beats 84.45%
# Memory: 20.20 MB Beats 6.71%
