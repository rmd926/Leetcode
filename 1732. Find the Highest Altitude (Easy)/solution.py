class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        temp = 0
        ans = temp
        for num in gain:
            temp += num
            ans = max(ans, temp)

        return ans

# Runtime: 0 ms Beats 100.00 %
# Memory: 19.40 MB Beats 10.37 %
