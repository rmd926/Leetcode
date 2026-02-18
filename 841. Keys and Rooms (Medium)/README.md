# 841. Keys and Rooms (Medium)

## Problem Description
There are `n` rooms labeled from `0` to `n - 1`. All rooms are locked except room `0`. Your goal is to visit **all** rooms, but you can only enter a locked room if you have its key.

When you visit room `i`, you may find a set of **distinct keys** inside it. Each key is an integer that represents the room it unlocks, and you can take all keys with you.

Given an array `rooms` where `rooms[i]` is the list of keys you can obtain after visiting room `i`, return `true` if you can visit all rooms, otherwise return `false`.

---

## Examples

### Example 1
**Input:** `rooms = [[1],[2],[3],[]]`  
**Output:** `true`  

**Explanation:**  
- Visit room `0`, get key `1`  
- Visit room `1`, get key `2`  
- Visit room `2`, get key `3`  
- Visit room `3`  
All rooms are visited.

### Example 2
**Input:** `rooms = [[1,3],[3,0,1],[2],[0]]`  
**Output:** `false`  

**Explanation:**  
Room `2` cannot be entered because the only key to room `2` is inside room `2` itself.

---

## Constraints
- `n == rooms.length`
- `2 <= n <= 1000`
- `0 <= rooms[i].length <= 1000`
- `1 <= sum(rooms[i].length) <= 3000`
- `0 <= rooms[i][j] < n`
- All values in `rooms[i]` are unique
