# 2300. Successful Pairs of Spells and Potions (Medium)

## Problem Description
You are given two positive integer arrays `spells` and `potions`, of length `n` and `m` respectively, where `spells[i]` represents the strength of the `i`-th spell and `potions[j]` represents the strength of the `j`-th potion.

You are also given an integer `success`. A pair `(spell, potion)` is considered **successful** if the product of their strengths is at least `success`, i.e.:
- `spells[i] * potions[j] >= success`

Return an integer array `pairs` of length `n` where `pairs[i]` is the number of potions that will form a successful pair with the `i`-th spell.

---

## Examples

### Example 1
**Input:** `spells = [5,1,3]`, `potions = [1,2,3,4,5]`, `success = 7`  
**Output:** `[4,0,3]`

**Explanation:**
- Spell 0: `5 * [1,2,3,4,5] = [5,10,15,20,25]` → `4` successful pairs  
- Spell 1: `1 * [1,2,3,4,5] = [1,2,3,4,5]` → `0` successful pairs  
- Spell 2: `3 * [1,2,3,4,5] = [3,6,9,12,15]` → `3` successful pairs  

So the result is `[4,0,3]`.

### Example 2
**Input:** `spells = [3,1,2]`, `potions = [8,5,8]`, `success = 16`  
**Output:** `[2,0,2]`

**Explanation:**
- Spell 0: `3 * [8,5,8] = [24,15,24]` → `2` successful pairs  
- Spell 1: `1 * [8,5,8] = [8,5,8]` → `0` successful pairs  
- Spell 2: `2 * [8,5,8] = [16,10,16]` → `2` successful pairs  

So the result is `[2,0,2]`.

---

## Constraints
- `n == spells.length`
- `m == potions.length`
- `1 <= n, m <= 10^5`
- `1 <= spells[i], potions[j] <= 10^5`
- `1 <= success <= 10^10`
