# 2651. Calculate Delayed Arrival Time (Easy)

## Problem Description
You are given two positive integers:

- `arrivalTime`: the scheduled arrival time of a train in hours
- `delayedTime`: the delay in hours

Return the time when the train will arrive at the station after the delay.

### Notes
- Time is in **24-hour format**.
- If the sum goes beyond 23, it should wrap around (mod 24).

---

## Examples

### Example 1
**Input:** `arrivalTime = 15`, `delayedTime = 5`  
**Output:** `20`

**Explanation:**  
The train was scheduled to arrive at `15:00` and is delayed by `5` hours.  
New arrival time = `15 + 5 = 20` (`20:00`).

### Example 2
**Input:** `arrivalTime = 13`, `delayedTime = 11`  
**Output:** `0`

**Explanation:**  
New arrival time = `13 + 11 = 24`, which is `00:00` in 24-hour format, so return `0`.

---

## Constraints
- `1 <= arrivalTime < 24`
- `1 <= delayedTime <= 24`
