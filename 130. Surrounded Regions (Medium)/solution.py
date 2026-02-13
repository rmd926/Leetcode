from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])

        def dfs(r: int, c: int) -> None:
            # 越界或不是 'O' 就停
            if r < 0 or r == ROWS or c < 0 or c == COLS or board[r][c] != "O":
                return

            # 先標記成暫存符號，表示「這個 O 是安全的（連到邊界）」
            board[r][c] = "T"

            # 往四方向擴展
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # 1) 只從邊界的 O 開始 DFS，把所有連到邊界的 O 標成 T
        for r in range(ROWS):
            dfs(r, 0)
            dfs(r, COLS - 1)

        for c in range(COLS):
            dfs(0, c)
            dfs(ROWS - 1, c)

        # 2) 全圖掃一次：
        #    - 剩下的 'O' 一定是被包圍的 -> 變 'X'
        #    - 'T' 是安全的 -> 變回 'O'
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"

                elif board[r][c] == "T":
                    board[r][c] = "O"

# Runtime: 0 ms Beats 100.00 %
# Memory: 22.44 MB Beats 43.67 %
