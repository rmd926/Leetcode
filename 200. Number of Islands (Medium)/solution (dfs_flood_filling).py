class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        ans = 0

        # Flood-Filling Algorithm
        def dfs(r, c):
            if r < 0 or r == rows or c < 0 or c == cols or grid[r][c] == "0" or (r, c) in visited:
                return False
            visited.add((r, c))
            # 需要四個方向都有走過才能return True
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

            return True
            
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c):
                    ans += 1
        
        return ans

# Runtime: 247 ms Beats 51.74 %
# Memory: 31.11 MB Beats 8.28 %
