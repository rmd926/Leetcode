# 121. Best Time to Buy and Sell Stock (Easy)

## Problem Description
You are given an array `prices` where `prices[i]` represents the price of a given stock on the `i`-th day.

You want to **maximize your profit** by choosing:
- **one day** to buy one stock, and
- a **different day in the future** to sell that stock.

Return the **maximum profit** you can achieve from this single transaction.  
If you cannot achieve any profit, return `0`.

> Note: You must buy the stock **before** you sell it.

---

## Examples

### Example 1
**Input:** `prices = [7,1,5,3,6,4]`  
**Output:** `5`  

**Explanation:**  
Buy on day 2 (price = `1`) and sell on day 5 (price = `6`).  
Profit = `6 - 1 = 5`.

---

### Example 2
**Input:** `prices = [7,6,4,3,1]`  
**Output:** `0`  

**Explanation:**  
No transaction is profitable, so the maximum profit is `0`.

---

## Constraints
- `1 <= prices.length <= 10^5`
- `0 <= prices[i] <= 10^4`
