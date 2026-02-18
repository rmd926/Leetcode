# 547. Number of Provinces (Medium)

## Problem Description
There are `n` cities. Some cities are directly connected, and some are not. If city `a` is directly connected to city `b`, and city `b` is directly connected to city `c`, then city `a` is **indirectly** connected to city `c`.

A **province** is a group of cities that are connected **directly or indirectly**, and there are no other cities outside the group.

You are given an `n x n` matrix `isConnected` where:
- `isConnected[i][j] = 1` if city `i` and city `j` are directly connected
- `isConnected[i][j] = 0` otherwise

Return the total number of provinces.

---

## Examples

### Example 1
**Input:** `isConnected = [[1,1,0],[1,1,0],[0,0,1]]`  
**Output:** `2`

### Example 2
**Input:** `isConnected = [[1,0,0],[0,1,0],[0,0,1]]`  
**Output:** `3`

---

## Constraints
- `1 <= n <= 200`
- `n == isConnected.length`
- `n == isConnected[i].length`
- `isConnected[i][j]` is `0` or `1`
- `isConnected[i][i] == 1`
- `isConnected[i][j] == isConnected[j][i]`
