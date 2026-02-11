class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        res = 0

        def dfs(r, c):
            if r < 0 or r == rows or c < 0 or c == cols or grid[r][c] == 0 or (r, c) in visited:
                return 0

            visited.add((r, c))
            return grid[r][c] + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)

        for r in range(rows):
            for c in range(cols):
                temp = dfs(r, c)
                if temp > 0 and temp % k == 0:
                    res += 1  
        return res

# Runtime: 442 ms Beats 34.59 %
# Memory: 119.43 MB Beats 5.67 %
