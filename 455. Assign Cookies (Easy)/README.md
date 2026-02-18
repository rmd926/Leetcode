# 455. Assign Cookies (Easy)

## Problem Description
You want to give cookies to children. Each child can receive **at most one** cookie.

- Each child `i` has a **greed factor** `g[i]`, meaning the child is satisfied only if the cookie size is **at least** `g[i]`.
- Each cookie `j` has a size `s[j]`.
- If `s[j] >= g[i]`, you can assign cookie `j` to child `i`, and that child becomes content.

Return the **maximum number of content children** you can achieve.

---

## Examples

### Example 1
**Input:** `g = [1,2,3]`, `s = [1,1]`  
**Output:** `1`  
**Explanation:** Only one child (greed `1`) can be satisfied because both cookies have size `1`.

### Example 2
**Input:** `g = [1,2]`, `s = [1,2,3]`  
**Output:** `2`  
**Explanation:** Cookie sizes are sufficient to satisfy both children.

---

## Constraints
- `1 <= g.length <= 3 * 10^4`
- `0 <= s.length <= 3 * 10^4`
- `1 <= g[i], s[j] <= 2^31 - 1`

---

## Note
This problem is the same as **2410. Maximum Matching of Players With Trainers**.
