# 328. Odd Even Linked List (Medium)

## Problem Description
Given the head of a singly linked list, reorder the list so that all nodes at **odd indices** are grouped together, followed by all nodes at **even indices**.

- The **first** node is considered **odd**, the **second** node is **even**, and so on.
- The **relative order** within the odd-indexed group and within the even-indexed group must remain the same as in the original list.

Return the reordered linked list.

You must solve the problem in:
- **O(1)** extra space
- **O(n)** time

---

## Examples

### Example 1
**Input:** `head = [1, 2, 3, 4, 5]`  
**Output:** `[1, 3, 5, 2, 4]`

### Example 2
**Input:** `head = [2, 1, 3, 5, 6, 4, 7]`  
**Output:** `[2, 3, 6, 7, 1, 5, 4]`

---

## Constraints
- The number of nodes in the linked list is in the range `[0, 10^4]`
- `-10^6 <= Node.val <= 10^6`
