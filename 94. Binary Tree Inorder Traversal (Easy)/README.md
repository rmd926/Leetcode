# 94. Binary Tree Inorder Traversal (Easy)

## Problem Description
Given the root of a binary tree, return the **inorder traversal** of its nodes' values.

Inorder traversal visits nodes in this order:
1. Left subtree
2. Node itself
3. Right subtree

---

## Examples

### Example 1
**Input:** `root = [1, null, 2, 3]`  
**Output:** `[1, 3, 2]`

### Example 2
**Input:** `root = [1,2,3,4,5,null,8,null,null,6,7,9]`  
**Output:** `[4, 2, 6, 5, 7, 1, 3, 9, 8]`

### Example 3
**Input:** `root = []`  
**Output:** `[]`

### Example 4
**Input:** `root = [1]`  
**Output:** `[1]`

---

## Constraints
- The number of nodes in the tree is in the range `[0, 100]`
- `-100 <= Node.val <= 100`

---

## Follow Up
A recursive solution is straightforward. Can you implement the inorder traversal **iteratively**?
