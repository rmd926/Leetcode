class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        lookup = {}

        for num in nums:
            if num not in lookup:
                lookup[num] = 1
            else:
                lookup[num] += 1

        max_freq = max(lookup.values())

        ans = 0

        for num in lookup:
            if lookup[num] == max_freq:
                ans += lookup[num]

        return ans

# Runtime: 0 ms Beats 100.00 %
# Memory: 19.38 MB Beats 24.91 %
