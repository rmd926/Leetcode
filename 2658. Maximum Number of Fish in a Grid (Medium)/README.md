# 2658. Maximum Number of Fish in a Grid (Medium)

## Problem Description
You are given a 0-indexed 2D matrix `grid` of size `m x n`, where each cell `(r, c)` represents:

- A **land cell** if `grid[r][c] = 0`, or
- A **water cell** containing `grid[r][c]` fish if `grid[r][c] > 0`.

A fisher can start at any water cell `(r, c)` and can perform the following operations any number of times:

- Catch all the fish at cell `(r, c)`, or
- Move to any **adjacent water cell**.

Return the **maximum number of fish** the fisher can catch if he chooses his starting cell optimally, or `0` if no water cell exists.

Adjacent cells to `(r, c)` are `(r, c + 1)`, `(r, c - 1)`, `(r + 1, c)`, `(r - 1, c)` (if they exist).

---

## Examples

### Example 1
**Input:** `grid = [[0,2,1,0],[4,0,0,3],[1,0,0,4],[0,3,2,0]]`  
**Output:** `7`

**Explanation:**  
The fisher can start at cell `(1,3)` and collect `3` fish, then move to cell `(2,3)` and collect `4` fish, for a total of `7`.

### Example 2
**Input:** `grid = [[1,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,1]]`  
**Output:** `1`

**Explanation:**  
The fisher can start at `(0,0)` or `(3,3)` and collect `1` fish.

---

## Constraints
- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 10`
- `0 <= grid[i][j] <= 10`
