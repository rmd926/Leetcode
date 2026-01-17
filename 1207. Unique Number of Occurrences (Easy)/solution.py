class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        lookup = {}
        for num in arr:
            if num not in lookup:
                lookup[num] = 1
            else:
                lookup[num] += 1

        ans = []
        for key, value in lookup.items():
            ans.append(value) # 把所有的次數都加進來，最後用set判斷是否有次數的值是重複的
        return len(ans) == len(set(ans))

# Runtime: 0 ms Beats 100.00 %
# Memory: 19.48 MB Beats 8.28%
