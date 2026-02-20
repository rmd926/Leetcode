# 142. Linked List Cycle II (Medium)

## Problem Description
Given the `head` of a singly linked list, return the **node where the cycle begins**.  
If there is **no cycle**, return `null`.

A cycle exists in a linked list if some node can be reached again by continuously following the `next` pointer.

Internally, `pos` is used to denote the index (0-indexed) of the node that the tail's `next` pointer connects to:
- `pos = -1` means there is **no cycle**
- `pos` is **not** passed as a parameter in the function

**Do not modify the linked list.**

---

## Examples

### Example 1
**Input:** `head = [3,2,0,-4]`, `pos = 1`  
**Output:** `tail connects to node index 1`  
**Explanation:** The tail connects to the second node, forming a cycle.

### Example 2
**Input:** `head = [1,2]`, `pos = 0`  
**Output:** `tail connects to node index 0`  
**Explanation:** The tail connects to the first node, forming a cycle.

### Example 3
**Input:** `head = [1]`, `pos = -1`  
**Output:** `no cycle`  
**Explanation:** There is no cycle in the linked list.

---

## Constraints
- The number of nodes is in the range `[0, 10^4]`
- `-10^5 <= Node.val <= 10^5`
- `pos` is `-1` or a valid index in the linked list

---

## Follow Up
Can you solve it using **O(1)** (constant) extra memory?
