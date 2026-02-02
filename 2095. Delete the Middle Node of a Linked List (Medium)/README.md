# 2095. Delete the Middle Node of a Linked List (Medium)

## Problem Description
You are given the head of a linked list. Delete the **middle node** of the linked list and return the head of the modified list.

The middle node of a linked list of size `n` is the **⌊n / 2⌋-th** node from the start using **0-based indexing**, where `⌊x⌋` denotes the floor of `x`.

For example, when `n = 1, 2, 3, 4, 5`, the middle node indices are:
- `0, 1, 1, 2, 2` respectively.

---

## Examples

### Example 1
**Input:** `head = [1,3,4,7,1,2,6]`  
**Output:** `[1,3,4,1,2,6]`

**Explanation:**  
`n = 7`, so the middle index is `⌊7/2⌋ = 3`.  
Remove the node at index `3` (value `7`).

### Example 2
**Input:** `head = [1,2,3,4]`  
**Output:** `[1,2,4]`

**Explanation:**  
`n = 4`, so the middle index is `⌊4/2⌋ = 2`.  
Remove the node at index `2` (value `3`).

### Example 3
**Input:** `head = [2,1]`  
**Output:** `[2]`

**Explanation:**  
`n = 2`, so the middle index is `⌊2/2⌋ = 1`.  
Remove the node at index `1` (value `1`).

---

## Constraints
- The number of nodes in the list is in the range `[1, 10^5]`
- `1 <= Node.val <= 10^5`
