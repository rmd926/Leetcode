class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        seq = list(map(str, nums))

        n = len(seq)

        for i in range(n):
            for j in range(i + 1, n):
                if seq[i] + seq[j] < seq[j] + seq[i]:
                    seq[i], seq[j] = seq[j], seq[i]

        ans = "".join(seq)

        if ans[0] == "0":
            return "0"

        return ans

# Runtime: 11 ms Beats 14.68 %
# Memory: 19.16 MB Beats 91.11 %
