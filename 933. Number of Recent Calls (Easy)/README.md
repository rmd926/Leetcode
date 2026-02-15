# 933. Number of Recent Calls (Easy)

## Problem Description
You need to implement a `RecentCounter` class that counts how many requests happened in a recent time window. Implement `RecentCounter()` to initialize the counter with zero requests, and `ping(t)` to add a new request at time `t` (milliseconds) and return the number of requests that occurred in the inclusive range `[t - 3000, t]` (including the new request). It is guaranteed that each call to `ping` uses a strictly increasing `t`.

## Example
**Input**


["RecentCounter", "ping", "ping", "ping", "ping"]
[[], [1], [100], [3001], [3002]]


**Output**


[null, 1, 2, 3, 3]


**Explanation**: `ping(1)` counts requests in `[-2999,1]` → 1; `ping(100)` counts in `[-2900,100]` → 2; `ping(3001)` counts in `[1,3001]` → 3; `ping(3002)` counts in `[2,3002]` → 3.

## Constraints
- `1 <= t <= 10^9`
- Each test case calls `ping` with strictly increasing `t`
- At most `10^4` calls will be made to `ping`
```
