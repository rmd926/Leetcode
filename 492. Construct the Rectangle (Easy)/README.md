
# 492. Construct the Rectangle (Easy)

## Problem
A web developer needs to know how to design a web page's size. Given a specific rectangular web page’s area, design a rectangle with length `L` and width `W` that satisfies:

1. The area of the rectangle equals the given `area`.
2. `L >= W` (width should not be larger than length).
3. The difference `L - W` is as small as possible.

Return an array `[L, W]` where `L` and `W` are the length and width of the designed web page.

---

## Examples

**Example 1**
- Input: `area = 4`
- Output: `[2,2]`
- Explanation: Possible pairs are `[1,4]`, `[2,2]`, `[4,1]`.  
  `[1,4]` violates `L >= W`, and `[4,1]` has a larger difference than `[2,2]`.  
  So the best is `[2,2]`.

**Example 2**
- Input: `area = 37`
- Output: `[37,1]`

**Example 3**
- Input: `area = 122122`
- Output: `[427,286]`

---

## Constraints
- `1 <= area <= 10^7`

