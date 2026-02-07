class Solution:
    def maximum69Number (self, num: int) -> int:
        num = list(str(num))
        for i in range(len(num)):
            if num[i] == "6":
                num[i] = "9"
                break
        return int("".join(num))

# Runtime: 0 ms Beats 100.00 %
# Memory: 19.45 MB Beats 9.70 %
