# 1448. Count Good Nodes in Binary Tree (Medium)

## Problem Description
Given the `root` of a binary tree, a node `X` is called **good** if on the path from the root to `X` (inclusive), there are **no nodes with a value greater than `X.val`**. In other words, `X` is good if `X.val` is **greater than or equal to** the maximum value seen along the path from the root to `X`. Return the total number of good nodes in the binary tree.

---

## Examples

### Example 1
**Input:** `root = [3,1,4,3,null,1,5]`  
**Output:** `4`  
**Explanation:**  
- The root `3` is always good.  
- Node `4` is good because it is the maximum on path `(3,4)`.  
- Node `5` is good because it is the maximum on path `(3,4,5)`.  
- Node `3` (left subtree) is good because it is the maximum on path `(3,1,3)`.

### Example 2
**Input:** `root = [3,3,null,4,2]`  
**Output:** `3`  
**Explanation:**  
Node `2` is not good because a larger value `3` appears earlier on the path `(3,3,2)`.

### Example 3
**Input:** `root = [1]`  
**Output:** `1`  
**Explanation:**  
The root is considered good.

---

## Constraints
- The number of nodes in the binary tree is in the range `[1, 10^5]`
- `-10^4 <= Node.val <= 10^4`
