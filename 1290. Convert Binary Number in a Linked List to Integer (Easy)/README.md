# 1290. Convert Binary Number in a Linked List to Integer (Easy)

## Problem Description
You are given `head`, a reference to the head node of a singly linked list.  
Each node in the linked list has a value of either `0` or `1`, and the list represents a binary number.

- The **most significant bit (MSB)** is at the head of the linked list.

Return the **decimal (base 10)** value of the binary number represented by the linked list.

---

## Examples

### Example 1
**Input:** `head = [1,0,1]`  
**Output:** `5`

**Explanation:**  
`(101)_2 = (5)_10`

### Example 2
**Input:** `head = [0]`  
**Output:** `0`

---

## Constraints
- The linked list is not empty
- The number of nodes will not exceed `30`
- Each node's value is either `0` or `1`
