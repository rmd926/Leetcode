class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        lookup = {}
        for char in words:
            if char not in lookup:
                lookup[char] = 1
            else:
                lookup[char] += 1

        ans = []
        for key, value in sorted(lookup.items(), key = lambda x: (-x[1], x[0])):
            ans.append(key)
            if len(ans) == k: # 避免掉冗餘的append，只要長度等於k之後就直接return ans
                return ans
