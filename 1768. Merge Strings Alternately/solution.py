class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n = min(len(word1), len(word2))
        ans = ""
        
        for i in range(n):
            ans += word1[i]
            ans += word2[i]
        
        if len(word2) > len(word1):
            ans += word2[n:]
        else:
            ans += word1[n:]
        
        return ans

'''
Performance Analysis:
-------------------------------
Time Complexity: O(m + n)
Space Complexity: O(m + n)
-------------------------------
Runtime: 42 ms Beats 75.60 %
Memory: 19.26 MB Beats 56.19 %
-------------------------------
'''
