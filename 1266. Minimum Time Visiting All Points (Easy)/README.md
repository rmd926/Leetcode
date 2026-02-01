# 1266. Minimum Time Visiting All Points (Easy)

## Problem Description
On a 2D plane, there are `n` points with integer coordinates `points[i] = [xi, yi]`.

Return the **minimum time in seconds** to visit all the points **in the given order**.

### Movement Rules
In **1 second**, you can:
- move **vertically** by 1 unit, or
- move **horizontally** by 1 unit, or
- move **diagonally** (equivalent to moving 1 unit vertically and 1 unit horizontally in the same second).

You must visit the points in the same order as they appear in `points`.

- You may pass through points that appear later in the order, but this does **not** count as visiting them.

---

## Examples

### Example 1
**Input:** `points = [[1,1],[3,4],[-1,0]]`  
**Output:** `7`

**Explanation:**  
One optimal path is:  
`[1,1] -> [2,2] -> [3,3] -> [3,4] -> [2,3] -> [1,2] -> [0,1] -> [-1,0]`

- Time from `[1,1]` to `[3,4]` = `3` seconds  
- Time from `[3,4]` to `[-1,0]` = `4` seconds  
- Total time = `7` seconds

### Example 2
**Input:** `points = [[3,2],[-2,2]]`  
**Output:** `5`

---

## Constraints
- `points.length == n`
- `1 <= n <= 100`
- `points[i].length == 2`
- `-1000 <= points[i][0], points[i][1] <= 1000`
