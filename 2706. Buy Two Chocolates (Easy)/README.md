# 2706. Buy Two Chocolates (Easy)

## Problem Description
You are given an integer array `prices` representing the prices of chocolates in a store, and an integer `money` representing your initial amount of money.

You must buy **exactly two** chocolates such that the remaining money is **non-negative**. You want to **minimize the sum** of the prices of the two chocolates you buy.

Return the amount of money left after buying the two chocolates. If it is not possible to buy two chocolates without going into debt, return `money`.

---

## Examples

### Example 1
**Input:** `prices = [1,2,2]`, `money = 3`  
**Output:** `0`

**Explanation:**  
Buy chocolates priced `1` and `2`. The total cost is `3`, so the leftover is `3 - 3 = 0`.

### Example 2
**Input:** `prices = [3,2,3]`, `money = 3`  
**Output:** `3`

**Explanation:**  
There is no way to buy two chocolates without going into debt, so return `3`.

---

## Constraints
- `2 <= prices.length <= 50`
- `1 <= prices[i] <= 100`
- `1 <= money <= 100`
