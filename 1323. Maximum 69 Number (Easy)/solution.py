# Method 1: One Line solution
class Solution:
    def maximum69Number (self, num: int) -> int:
        return int(str(num).replace("6", "9", 1))
# Runtime: 0 ms Beats 100.00 %
# Memory: 19.34 MB Beats 31.31 %

# Method 2:
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
