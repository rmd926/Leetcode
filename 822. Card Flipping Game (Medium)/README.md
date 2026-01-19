# 822. Card Flipping Game (Medium)

## Problem Description
You are given two 0-indexed integer arrays `fronts` and `backs` of length `n`, where the `i`-th card has the positive integer `fronts[i]` printed on the front and `backs[i]` printed on the back.

Initially, each card is placed on a table with its **front number facing up** and its **back number facing down**. You may flip over **any number of cards** (possibly zero).

After flipping, an integer is considered **good** if:
- it is facing **down** on **at least one** card, and
- it is facing **up** on **no** cards.

Return the **minimum possible good integer** after flipping some cards.  
If there are **no** good integers, return `0`.

---

## Examples

### Example 1
**Input:**  
`fronts = [1,2,4,4,7]`  
`backs  = [1,3,4,1,3]`  

**Output:** `2`

**Explanation:**  
If we flip the second card, the face-up numbers become `[1,3,4,4,7]` and the face-down numbers become `[1,2,4,1,3]`.  
`2` appears facing down but not facing up, so it is a good integer. It can be shown that `2` is the minimum possible good integer.

---

### Example 2
**Input:**  
`fronts = [1]`  
`backs  = [1]`  

**Output:** `0`

**Explanation:**  
No matter how we flip the card, there is no integer that can be good, so we return `0`.

---

## Constraints
- `n == fronts.length == backs.length`
- `1 <= n <= 1000`
- `1 <= fronts[i], backs[i] <= 2000`
