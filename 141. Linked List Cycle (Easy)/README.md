# 141. Linked List Cycle (Easy)

## Problem Description
Given `head`, the head of a linked list, determine whether the linked list contains a **cycle**.

A cycle exists if there is some node in the list that can be reached again by continuously following the `next` pointer.

Internally, `pos` is used to denote the index of the node that the tail’s `next` pointer connects to:
- `pos = -1` means there is **no cycle**
- `pos` is **not** passed as a parameter

Return `true` if there is a cycle in the linked list; otherwise, return `false`.

---

## Examples

### Example 1
**Input:** `head = [3,2,0,-4]`, `pos = 1`  
**Output:** `true`  
**Explanation:** The tail connects to the node at index `1` (0-indexed), forming a cycle.

### Example 2
**Input:** `head = [1,2]`, `pos = 0`  
**Output:** `true`  
**Explanation:** The tail connects to the node at index `0`, forming a cycle.

### Example 3
**Input:** `head = [1]`, `pos = -1`  
**Output:** `false`  
**Explanation:** There is no cycle in the linked list.

---

## Constraints
- Number of nodes is in the range `[0, 10^4]`
- `-10^5 <= Node.val <= 10^5`
- `pos` is `-1` or a valid index in the linked list

---

## Follow Up
Can you solve it using **O(1)** (constant) extra memory?
