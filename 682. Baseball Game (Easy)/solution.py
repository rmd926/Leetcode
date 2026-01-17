class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack = []
        for op in ops:
            if op == "C":
                stack.pop()
            
            elif op == "D":
                stack.append(stack[-1]*2)

            elif op == "+":
                stack.append(stack[-1]+stack[-2])

            else: 
                stack.append(int(op))

        return sum(stack)

# Runtime: 0 ms Beats 100.00 %
# Memory: 19.59 MB Beats 7.95 %
