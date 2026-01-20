class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for ast in asteroids:
            if ast > 0:
                stack.append(ast)
            else:
                # 當前最後一個 > 0，而且他比往負方向的體積小的時候，要pop掉
                while stack and stack[-1] > 0 and stack[-1] < -ast:
                    stack.pop()
                if stack and stack[-1] == -ast:
                    stack.pop()
                elif not stack or stack[-1] < 0:
                    stack.append(ast)
        
        return stack

# Runtime: 5 ms Beats 71.08 %
# Memory: 20.44 MB Beats 8.91 %        
