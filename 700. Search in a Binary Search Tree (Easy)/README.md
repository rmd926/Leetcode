# 700. Search in a Binary Search Tree (Easy)

## Problem Description
You are given the root of a Binary Search Tree (BST) and an integer `val`.

Find the node in the BST such that the node's value equals `val`, and return the **subtree rooted at that node**.  
If such a node does not exist, return `null`.

A BST satisfies:
- Values in the left subtree are **less than** the node's value.
- Values in the right subtree are **greater than** the node's value.

---

## Examples

### Example 1
**Input:** `root = [4,2,7,1,3]`, `val = 2`  
**Output:** `[2,1,3]`

**Explanation:**  
The node with value `2` exists in the tree, so return the subtree rooted at `2`.

### Example 2
**Input:** `root = [4,2,7,1,3]`, `val = 5`  
**Output:** `[]`

**Explanation:**  
No node with value `5` exists in the BST, so return `null`.

---

## Constraints
- The number of nodes in the tree is in the range `[1, 5000]`
- `1 <= Node.val <= 10^7`
- `root` is a binary search tree
- `1 <= val <= 10^7`
