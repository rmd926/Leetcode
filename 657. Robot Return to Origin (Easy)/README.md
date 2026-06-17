# 657. Robot Return to Origin (Easy)

## Problem

There is a robot starting at the position `(0, 0)`, the origin, on a 2D plane.

Given a string `moves`, determine whether the robot returns to the origin after completing all moves.

Each character in `moves` represents one move:

* `'R'`: move right
* `'L'`: move left
* `'U'`: move up
* `'D'`: move down

Return `true` if the robot returns to `(0, 0)`.
Otherwise, return `false`.

## Examples

### Example 1

```text
Input: moves = "UD"
Output: true
```

Explanation:

The robot moves up once and then down once.
These two moves cancel each other out, so the robot returns to the origin.

### Example 2

```text
Input: moves = "LL"
Output: false
```

Explanation:

The robot moves left twice.
It ends up two moves to the left of the origin, so it does not return to `(0, 0)`.

## Constraints

```text
1 <= moves.length <= 2 * 10^4
moves only contains the characters 'U', 'D', 'L', and 'R'.
```
