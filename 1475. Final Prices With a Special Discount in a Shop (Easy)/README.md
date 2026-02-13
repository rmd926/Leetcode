# 1475. Final Prices With a Special Discount in a Shop (Easy)

## Problem Description
You are given an integer array `prices` where `prices[i]` is the price of the `i`-th item in a shop.

There is a special discount rule: if you buy the `i`-th item, you will receive a discount equal to `prices[j]`, where `j` is the **smallest index** such that `j > i` and `prices[j] <= prices[i]`. If no such `j` exists, then the item receives **no discount**.

Return an integer array `answer` where `answer[i]` is the final price you pay for the `i`-th item after applying the discount rule.

---

## Examples

### Example 1
**Input:** `prices = [8,4,6,2,3]`  
**Output:** `[4,2,4,2,3]`

**Explanation:**  
- Item 0 (8) gets discount 4 (item 1) → `8 - 4 = 4`  
- Item 1 (4) gets discount 2 (item 3) → `4 - 2 = 2`  
- Item 2 (6) gets discount 2 (item 3) → `6 - 2 = 4`  
- Items 3 and 4 get no discount

### Example 2
**Input:** `prices = [1,2,3,4,5]`  
**Output:** `[1,2,3,4,5]`

**Explanation:**  
No item has a later item with price less than or equal to itself, so no discounts apply.

### Example 3
**Input:** `prices = [10,1,1,6]`  
**Output:** `[9,0,1,6]`

---

## Constraints
- `1 <= prices.length <= 500`
- `1 <= prices[i] <= 1000`
