class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        ans = []
        for i in range(len(words)):
            if x in words[i]:
                ans.append(i) 
            else:
                continue
        
        return ans
# Runtime: 0 ms Beats 100.00 %
# Memory: 19.41 MB Beats 20.96 %
