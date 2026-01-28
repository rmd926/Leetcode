# 2769. Find the Maximum Achievable Number (Easy)

## Problem Description
You are given two integers, `num` and `t`.

A number `x` is **achievable** if it can become equal to `num` after applying the following operation **at most `t` times**:

- Increase or decrease `x` by `1`, and **simultaneously** increase or decrease `num` by `1`.

Return the **maximum possible value** of `x`.

---

## Examples

### Example 1
**Input:** `num = 4`, `t = 1`  
**Output:** `6`

**Explanation:**  
Apply the operation once in a way that maximizes `x`.

### Example 2
**Input:** `num = 3`, `t = 2`  
**Output:** `7`

**Explanation:**  
Apply the operation twice in a way that maximizes `x`.

---

## Constraints
- `1 <= num, t <= 50`
