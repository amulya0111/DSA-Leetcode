# DPFIBONACCI - Rating 1050

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Fibonacci Series

Given an integer $N$, output the $N^{th}$ term in the Fibonacci Series.
The Fibonacci Series is: `0 1 1 2 3 5 8...`

Complete the function `fib()` function to solve this problem using  **recursion**.

### Input Format
- The input contains a single integer $N$.
### Output Format

Output the $N^{th}$ term in the Fibonacci Series.

### Constraints
- $1 \leq N \leq 100$
### Sample 1:
Input
Output

```
1
```

```
0
```

### Sample 2:
Input
Output

```
2
```

```
1
```

### Sample 3:
Input
Output

```
7
```

```
8
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-11-02T18:20:04.215Z  

```py
def fib(n):
    #Write your code here
    if n==1:
        return 0
    if n==2:
        return 1
    n= fib(n-1)+fib(n-2)
    return n
n = int(input())
print(fib(n))
```

---

[View on CodeChef](https://www.codechef.com/problems/DPFIBONACCI)