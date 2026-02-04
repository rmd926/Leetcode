# 2487. Remove Nodes From Linked List (Medium)

## Problem Description
You are given the head of a linked list.

Remove every node that has a node with a **greater value** anywhere to its **right** in the list.

Return the head of the modified linked list.

---

## Examples

### Example 1
**Input:** `head = [5,2,13,3,8]`  
**Output:** `[13,8]`

**Explanation:**  
Nodes to remove: `5`, `2`, and `3`
- `13` is to the right of `5` and `13 > 5`
- `13` is to the right of `2` and `13 > 2`
- `8` is to the right of `3` and `8 > 3`

### Example 2
**Input:** `head = [1,1,1,1]`  
**Output:** `[1,1,1,1]`

**Explanation:**  
All values are equal, so no nodes are removed.

---

## Constraints
- The number of nodes in the list is in the range `[1, 10^5]`
- `1 <= Node.val <= 10^5`
