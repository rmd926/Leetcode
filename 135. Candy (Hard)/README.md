# 135. Candy (Hard)

## Problem Description
There are `n` children standing in a line. Each child has a rating given in the integer array `ratings`.

You want to give candies to the children under these rules:
1. Each child must have **at least 1** candy.
2. Any child with a **higher rating** than a neighboring child must receive **more candies** than that neighbor.

Return the **minimum total number of candies** needed to satisfy these requirements.

---

## Examples

### Example 1
**Input:** `ratings = [1,0,2]`  
**Output:** `5`  
**Explanation:** One valid distribution is `[2,1,2]`, which sums to `5`.

### Example 2
**Input:** `ratings = [1,2,2]`  
**Output:** `4`  
**Explanation:** One valid distribution is `[1,2,1]`, which sums to `4`.  
The third child can have `1` candy because its rating is not higher than the second child's rating.

---

## Constraints
- `n == ratings.length`
- `1 <= n <= 2 * 10^4`
- `0 <= ratings[i] <= 2 * 10^4`
