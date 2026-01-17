class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_stack = []
        t_stack = []
        for ch in s:
            if ch == "#" and len(s_stack) != 0:# 避免掉pop empty
                s_stack.pop()

            elif ch == "#" and len(s_stack) == 0: # 如果第一個是#，不要丟到stack而是保持empty
                s_stack = s_stack

            elif ch != "#":
                s_stack.append(ch)
        
        for ch in t:
            if ch == "#" and len(t_stack) != 0:
                t_stack.pop()

            elif ch == "#" and len(t_stack) == 0: 
                t_stack = t_stack

            elif ch != "#":
                t_stack.append(ch)
        
        return s_stack == t_stack

# Runtime: 0 ms Beats 100.00 %
# Memory: 19.36 MB Beats 13.48 %
