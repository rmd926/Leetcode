# 79. Word Search (Medium)

## Problem Description
Given an `m x n` grid of characters `board` and a string `word`, return `true` if `word` exists in the grid. Otherwise, return `false`.

The word can be constructed from letters of **sequentially adjacent cells**, where adjacent cells are **horizontally or vertically** neighboring.

### Rules
- Each cell can be used **at most once** in forming the word.
- You may move **up, down, left, or right** between adjacent cells.

---

## Examples

### Example 1
**Input:**
`board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]`  
`word = "ABCCED"`  
**Output:** `true`

### Example 2
**Input:**
`board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]`  
`word = "SEE"`  
**Output:** `true`

### Example 3
**Input:**
`board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]`  
`word = "ABCB"`  
**Output:** `false`

---

## Constraints
- `m == board.length`
- `n == board[i].length`
- `1 <= m, n <= 6`
- `1 <= word.length <= 15`
- `board` and `word` consist only of lowercase and uppercase English letters

---

## Follow Up
Could you use search pruning to make your solution faster with a larger board?
