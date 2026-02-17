# 3663. Find The Least Frequent Digit (Easy)

## Problem Description
Given an integer `n`, find the digit that occurs **least frequently** in its decimal representation. If multiple digits have the same minimum frequency, choose the **smallest digit** among them. Return the chosen digit as an integer. The frequency of a digit `x` is the number of times it appears in the decimal representation of `n`.

## Examples
### Example 1
**Input:** `n = 1553322`  
**Output:** `1`  
**Explanation:** The digit `1` appears once, while all other digits appear twice, so `1` is the least frequent.

### Example 2
**Input:** `n = 723344511`  
**Output:** `2`  
**Explanation:** Digits `7`, `2`, and `5` each appear once (minimum frequency). The smallest among them is `2`.

## Constraints
- `1 <= n <= 2^31 - 1`
