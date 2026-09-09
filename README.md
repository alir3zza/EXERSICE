# Weird Number Checker

Exercise from [HackerRank](https://www.hackerrank.com/) — Python (Basic) section.

## Problem Statement

Given an integer `n`, perform the following conditional actions:

- If `n` is **odd**, print `Weird`
- If `n` is **even** and in the inclusive range of `2` to `5`, print `Not Weird`
- If `n` is **even** and in the inclusive range of `6` to `20`, print `Weird`
- If `n` is **even** and greater than `20`, print `Not Weird`

## Solution Code

```python
n = int(input())

if n % 2 != 0:
    print("Weird")
elif 2 <= n <= 5:
    print("Not Weird")
elif 6 <= n <= 20:
    print("Weird")
else:
    print("Not Weird")
```

## How to Run

```bash
python weird.py
```

Then enter an integer to see the output.

## Sample Input/Output

| Input | Output     | Reason                        |
|-------|------------|--------------------------------|
| 3     | Weird      | It's odd                       |
| 4     | Not Weird  | Even and between 2 and 5       |
| 10    | Weird      | Even and between 6 and 20      |
| 26    | Not Weird  | Even and greater than 20       |

## Notes

- Instead of four `if/elif` branches, the last case is better written with `else` (since all other cases are already covered).
- Use the `%` operator to check even/odd, not `/`.
