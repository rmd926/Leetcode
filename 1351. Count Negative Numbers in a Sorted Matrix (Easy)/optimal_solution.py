from typing import List

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        r, c = 0, COLS - 1
        ans = 0

        while r < ROWS and c >= 0: # 因為是由大到小排列，所以檢查負號要往左搜
            if grid[r][c] < 0:
                ans += (ROWS - r) # r到目前這行結束都是負的
                c -= 1 # 往左檢查
            else:
                r += 1 # 跳到下一行
        
        return ans 

# Runtime: 0 ms Beats 100.00 %
# Memory: 20.29 MB Beats 9.66 %
