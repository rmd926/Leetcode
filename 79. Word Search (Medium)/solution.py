class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])
        visited = set()

        def dfs(row, col, index):
            if index == len(word):
                return True
            # 邊界判斷
            if row < 0 or row == ROWS or col < 0 or col == COLS or (row, col) in visited or board[row][col] != word[index]:
                return False
            visited.add((row, col))
            # 四個方向遞迴判斷
            if dfs(row+1, col, index+1) or dfs(row-1, col, index+1) or dfs(row, col+1, index+1) or dfs(row, col-1, index+1):
                return True
            visited.remove((row, col))
            return False

        for row in range(ROWS):
            for col in range(COLS):
                if dfs(row, col, 0):
                    return True
        return False

# Runtime: 4313 ms Beats 38.98 %
# Memory: 19.60 MB Beats 37.58 %
