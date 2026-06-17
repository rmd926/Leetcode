class Solution:
    def judgeCircle(self, moves: str) -> bool:
        pos = [0, 0]
        for ch in moves:
            if ch == "R":
                pos[0] += 1
            elif ch == "L":
                pos[0] -= 1
            elif ch == "U":
                pos[1] += 1
            elif ch == "D":
                pos[1] -= 1
        
        return pos == [0, 0]

# Runtime: 19 ms Beats 26.58 %
# Memory: 19.31 MB Beats 21.64 %
