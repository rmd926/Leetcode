# 130. Surrounded Regions (Medium)

## Problem Description
You are given an `m x n` matrix `board` containing characters `'X'` and `'O'`. Capture all regions that are surrounded.

- **Connect:** A cell is connected to adjacent cells horizontally or vertically.
- **Region:** A region is formed by connecting adjacent `'O'` cells.
- **Surround:** A region is surrounded if none of its `'O'` cells are on the edge of the board (i.e., it is completely enclosed by `'X'` cells).

To capture a surrounded region, replace all `'O'` cells in that region with `'X'` **in-place**. You do not need to return anything.

---

## Examples

### Example 1
**Input:** `board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]`  
**Output:** `[["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]`

**Explanation:**  
The bottom `'O'` region is not captured because it touches the edge of the board and cannot be surrounded.

### Example 2
**Input:** `board = [["X"]]`  
**Output:** `[["X"]]`

---

## Constraints
- `m == board.length`
- `n == board[i].length`
- `1 <= m, n <= 200`
- `board[i][j]` is `'X'` or `'O'`
