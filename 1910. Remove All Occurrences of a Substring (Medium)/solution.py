class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []
        m = len(part)

        for char in s:
            stack.append(char)
            # list1 = ["a", "b", "a", "b", "c"] => "".join(list1)

            if len(stack) >= m and "".join(stack[-m:]) == part:
                for i in range(m): # 把stack最尾端(長度為m的)部分pop掉
                    stack.pop()
        return "".join(stack)

# Runtime: 15 ms Beats 29.17 %
# Memory: 19.40 MB Beats 44.09 %
