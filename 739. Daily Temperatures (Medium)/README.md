# 739. Daily Temperatures (Medium)

## Problem Description
Given an array of integers `temperatures` where `temperatures[i]` represents the temperature on the `i`-th day, return an array `answer` such that:

- `answer[i]` is the number of days you have to wait **after the `i`-th day** to get a **warmer temperature**.
- If there is **no future day** with a warmer temperature, then `answer[i] = 0`.

---

## Examples

### Example 1
**Input:**  
`temperatures = [73,74,75,71,69,72,76,73]`  

**Output:**  
`[1,1,4,2,1,1,0,0]`

**Explanation:**  
- Day 0 (73) → warmer on day 1 (74), wait 1 day  
- Day 2 (75) → warmer on day 6 (76), wait 4 days  
- Day 6 (76) → no warmer future day, so 0  

---

### Example 2
**Input:**  
`temperatures = [30,40,50,60]`  

**Output:**  
`[1,1,1,0]`

**Explanation:**  
Each day has a warmer temperature the next day, except the last.

---

### Example 3
**Input:**  
`temperatures = [30,60,90]`  

**Output:**  
`[1,1,0]`

---

## Constraints
- `1 <= temperatures.length <= 10^5`
- `30 <= temperatures[i] <= 100`
