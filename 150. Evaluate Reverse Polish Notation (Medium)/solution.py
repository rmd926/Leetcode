class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        left, right = 0, 0
        stack = []
        temp = 0
        for t in tokens:
            if t == "+":
                right = int(stack.pop())
                left = int(stack.pop())
                stack.append(left+right)
            
            elif t == "-":
                right = int(stack.pop())
                left = int(stack.pop())
                stack.append(left-right)
            
            elif t == "*":
                right = int(stack.pop())
                left = int(stack.pop())
                stack.append(left*right)

            elif t == "/":
                right = int(stack.pop())
                left = int(stack.pop())
                stack.append(int(left/right)) # 因為是truncate toward zero，不能使用//
            
            else:
                stack.append(int(t))

        return stack.pop()

# Runtime: 0 ms Beats 100.00 %
# Memory: 20.60 MB Beats 21.78 %
