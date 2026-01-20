class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for vol in asteroids:
            if vol > 0:
                stack.append(vol)
            else:
                # 當前最後一個 > 0，而且他比往負方向的體積小的時候，要pop掉
                while stack and stack[-1] > 0 and stack[-1] < abs(vol):
                    stack.pop()
                # 如果stack還有東西且最後一個值恰好 和反方向的體積相同，兩者會一起爆炸 (僅需要pop掉在原本stack的最後一個)
                if stack and stack[-1] == abs(vol):
                    stack.pop()
                # 如果stack is empty 或者是最後一個元素也 < 0，那就把他append到stack裡面
                elif not stack or stack[-1] < 0:
                    stack.append(vol)

        return stack

# Runtime: 3 ms Beats 94.65 %
# Memory: 20.40 MB Beats 17.79 %        
