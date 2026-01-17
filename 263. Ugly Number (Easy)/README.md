# 263. Ugly Number (Easy)

## Problem Description
An **ugly number** is a **positive integer** whose **prime factors** include **only** `2`, `3`, and `5`.

Given an integer `n`, return `true` if `n` is an ugly number, and `false` otherwise.

> Note: The number `1` is considered an ugly number because it has no prime factors.

---

## Examples

### Example 1
**Input:** `n = 6`  
**Output:** `true`  

**Explanation:**  
`6 = 2 × 3`, and its prime factors are only `2` and `3`.

---

### Example 2
**Input:** `n = 1`  
**Output:** `true`  

**Explanation:**  
`1` has no prime factors, so it is considered an ugly number.

---

### Example 3
**Input:** `n = 14`  
**Output:** `false`  

**Explanation:**  
`14 = 2 × 7`, which includes the prime factor `7`, so it is not an ugly number.

---

## Constraints
- `-2^31 <= n <= 2^31 - 1`
