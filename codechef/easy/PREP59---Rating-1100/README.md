# PREP59 - Rating 1100

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Valid Parenthesis

If you are new to stacks and queues, or want a refresher on them, start with our Learn Stacks and Queues course

Give string a $S$ consisting of only $($ and $)$. Find whether $S$ is a valid parenthesis string.

Note: A  **valid parentheses**  string is defined as:

- Empty string is valid.
- If $P$ is valid, $(P)$ is also valid.
- If $P$ and $Q$ are valid, $PQ$ is also valid.
### Input Format
- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of a single line of input, containing string $S$.
### Output Format

For each test case, output $1$ if the given string is a valid parenthesis, or output $0$ otherwise.

### Constraints
- $1 \leq T \leq 100$
- $1 \leq |S| \leq 10^5$
- The sum of $|S|$ over all test cases won't exceed $2 \cdot 10^5$.
### Sample 1:
Input
Output

```
3
()(())
(()()
))((

```

```
1
0
0

```

### Explanation:

 **Test case $1$** : $()(())$ will be valid parenthesis.

 **Test case $2$** : $(()()$ will not be valid parenthesis.

 **Test case $3$** : $))(($ will not be valid parenthesis.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-18T16:44:35.832Z  

```py
def is_valid_parentheses(s):
    balance = 0
    for char in s:
        if char == '(':
            balance += 1
        else:  # char == ')'
            if balance == 0:
                return False
            balance -= 1
    return balance == 0

def main():
    import sys
    input_data = sys.stdin.read().strip().split()
    if not input_data: 
        return
    t = int(input_data[0])
    results = []
    for i in range(1, t + 1):
        s = input_data[i]
        if is_valid_parentheses(s):
            results.append("1")
        else:
            results.append("0")
    sys.stdout.write("\n".join(results))

if __name__ == "__main__":
    main()
```

---

[View on CodeChef](https://www.codechef.com/problems/PREP59)