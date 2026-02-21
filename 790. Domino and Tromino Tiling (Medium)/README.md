# 790. Domino and Tromino Tiling (Medium)

## Problem Description
You are given a **2 × n** board and two kinds of tiles:

- **Domino**: size **2 × 1** (can be rotated to **1 × 2**)
- **Tromino**: an **L-shape** covering **3** cells (can be rotated)

Your task is to count how many different ways can **tile the entire 2 × n board** so that:

- Every cell is covered by exactly one tile
- Tiles may be rotated
- Two tilings are different if there exists at least one pair of adjacent cells such that exactly one tiling places them inside the same tile

Because the answer can be very large, return it **modulo** `10^9 + 7`.

---

## Examples

### Example 1
**Input:** `n = 3`  
**Output:** `5`

**Explanation:** There are 5 distinct tilings for a 2×3 board.

### Example 2
**Input:** `n = 1`  
**Output:** `1`

---

## Constraints
- `1 <= n <= 1000`

---
