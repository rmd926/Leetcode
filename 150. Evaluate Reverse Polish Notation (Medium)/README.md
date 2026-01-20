# 150. Evaluate Reverse Polish Notation (Medium)

## Problem Description
You are given an array of strings `tokens` that represents an arithmetic expression written in **Reverse Polish Notation (RPN)**.

Your task is to **evaluate the expression** and return the resulting integer value.

---

## Notes
- Valid operators are: `+`, `-`, `*`, `/`
- Each operand may be an integer or the result of another expression
- Division between two integers **always truncates toward zero**
- Division by zero will never occur
- The input is guaranteed to be a valid RPN expression
- All intermediate values and the final answer fit within a 32-bit integer

---

## Examples

### Example 1
**Input:**  
`tokens = ["2","1","+","3","*"]`  

**Output:**  
`9`

**Explanation:**  
`
((2 + 1) * 3) = 9
`

---

### Example 2
**Input:**  
`tokens = ["4","13","5","/","+"]`  

**Output:**  
`6`

**Explanation:**  

`
4 + (13 / 5) = 4 + 2 = 6
`


---

### Example 3
**Input:**  
`tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]`  

**Output:**  
`22`

**Explanation:**  

`
((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= 22
`


---

## Constraints
- `1 <= tokens.length <= 10^4`
- `tokens[i]` is either an operator (`+`, `-`, `*`, `/`) or an integer in the range `[-200, 200]`

