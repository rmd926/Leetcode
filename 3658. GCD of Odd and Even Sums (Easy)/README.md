# 3658. GCD of Odd and Even Sums (Easy)

## Problem Description
You are given an integer `n`. Compute the GCD (greatest common divisor) of the following two values:

- `sumOdd`: the sum of the smallest `n` positive odd numbers.
- `sumEven`: the sum of the smallest `n` positive even numbers.

Return `gcd(sumOdd, sumEven)`.

---

## Examples

### Example 1
**Input:** `n = 4`  
**Output:** `4`

**Explanation:**
- `sumOdd = 1 + 3 + 5 + 7 = 16`
- `sumEven = 2 + 4 + 6 + 8 = 20`
- `gcd(16, 20) = 4`

### Example 2
**Input:** `n = 5`  
**Output:** `5`

**Explanation:**
- `sumOdd = 1 + 3 + 5 + 7 + 9 = 25`
- `sumEven = 2 + 4 + 6 + 8 + 10 = 30`
- `gcd(25, 30) = 5`

---

## Constraints
- `1 <= n <= 1000`
