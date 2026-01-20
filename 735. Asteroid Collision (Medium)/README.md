# 735. Asteroid Collision (Medium)

## Problem Description
You are given an integer array `asteroids` representing asteroids moving in a straight line. The index of each asteroid represents its relative position in space.

For each asteroid:
- The **absolute value** represents its **size**
- The **sign** represents its **direction**
  - Positive (`+`) means moving **right**
  - Negative (`-`) means moving **left**

All asteroids move at the same speed.

When two asteroids collide:
- The **smaller** asteroid explodes
- If both are the **same size**, **both** explode
- Asteroids moving in the **same direction** will **never** meet

Return the state of the asteroids after all collisions.

---

## Examples

### Example 1
**Input:** `asteroids = [5,10,-5]`  
**Output:** `[5,10]`

**Explanation:**  
`10` and `-5` collide, `-5` explodes. `5` and `10` never collide.

---

### Example 2
**Input:** `asteroids = [8,-8]`  
**Output:** `[]`

**Explanation:**  
Both asteroids have the same size, so both explode.

---

### Example 3
**Input:** `asteroids = [10,2,-5]`  
**Output:** `[10]`

**Explanation:**  
`2` and `-5` collide → `2` explodes. Then `10` and `-5` collide → `-5` explodes.

---

### Example 4
**Input:** `asteroids = [3,5,-6,2,-1,4]`  
**Output:** `[-6,2,4]`

**Explanation:**  
`-6` destroys `5` and `3` and continues moving left.  
`2` destroys `-1` and continues moving right without reaching `4`.

---

## Constraints
- `2 <= asteroids.length <= 10^4`
- `-1000 <= asteroids[i] <= 1000`
- `asteroids[i] != 0`
