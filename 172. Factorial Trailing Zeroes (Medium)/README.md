# 172. Factorial Trailing Zeroes (Medium)

## Problem Description
Given an integer `n`, return the number of **trailing zeroes** in `n!`.

The factorial `n!` is defined as:
`n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1`

A trailing zero is a `0` at the end of the number.

---

## Examples

### Example 1
**Input:** `n = 3`  
**Output:** `0`  
**Explanation:** `3! = 6`, which has no trailing zero.

### Example 2
**Input:** `n = 5`  
**Output:** `1`  
**Explanation:** `5! = 120`, which has one trailing zero.

### Example 3
**Input:** `n = 0`  
**Output:** `0`

---

## Constraints
- `0 <= n <= 10^4`

---

## Follow Up
Can you write a solution that works in **logarithmic time complexity**?
