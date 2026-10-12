# MSTEX

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Most Expensive Items

Chef is given the prices of $N$ items and wants to buy exactly $K$ of them.

Find the  **maximum possible total price**  of the $K$ items he can choose.

### Input Format

The first line contains an integer $T$ — the number of test cases.

For each test case:

- The first line contains two space-separated integers $N$ and $K$ — the number of items and the number of items Chef wants to buy.
- The second line contains $N$ space-separated integers $C_1,C_2,\ldots,C_N$ — the prices of the items.
### Output Format

For each test case, print a single integer — the total cost of the $K$ most expensive items.

### Constraints
- $1 \le T \le 100$
- $1 \le K \le N \le 100$
- $1 \le C_i \le 100$
### Sample 1:
Input
Output

```
3
5 2
4 9 1 7 6
4 3
10 3 8 5
6 1
2 11 4 9 7 5
```

```
16
23
11
```

### Explanation:

For the first test case, the two highest prices are $9$ and $7$.

$9+7=16$

For the second test case, the three highest prices are $10$, $8$, and $5$.

$10+8+5=23$

For the third test case, Chef buys only the most expensive item, which costs $11$.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-12T16:22:16.456Z  

```py
# cook your dish here

```

---

[View on CodeChef](https://www.codechef.com/problems/MSTEX)