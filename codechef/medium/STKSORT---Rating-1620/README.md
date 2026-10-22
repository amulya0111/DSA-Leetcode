# STKSORT - Rating 1620

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Stack Sort

You have an array $A$ of integers of size $N$, an array $B$ (initially empty) and a stack $S$ (initially empty). You are allowed to do the following operations :

- Take the first element of array $A$ and push it into $S$ and remove it from $A$.
- Take the top element from stack $S$, append it to the end of array $B$ and remove it from $S$.

You have to tell if it possible to move all the elements of array $A$ to array $B$ using the above operations such that finally the array $B$ is sorted in ascending order.

### Input Format
- First line will contain $T$, number of testcases. Then the testcases follow.
- First line of each testcase contains a single integer $N$.
- Second line of each testcase contains $N$ distinct integers : $A_1, A_2... A_N$.
### Output Format

For each testcase, if it possible to move all the elements of array $A$ to array $B$ using the above operations such that finally, the array $B$ is sorted in ascending order, print "YES" (without quotes), else print "NO" (without quotes).

### Constraints
- $1 \leq T \leq 100$
- $1 \leq N \leq 10^5$
- $1 \leq A_i \leq N$
- $A_i = A_j$ if and only if $i = j$

It is guaranteed that the sum of values of $N$ over all the test cases doesn't exceed $2*10^6$.

### Subtasks
- 30 points : $1 \leq N \leq 500$
- 70 points : original constraints
### Sample 1:
Input
Output

```
2
4
1 2 4 3
4
1 3 4 2
```

```
YES
NO
```

### Explanation:

 **Test-case 1:**  Consider the following sequence of operations

- Remove $1$ from $A$ and push it into $S$.
- Remove $1$ from $S$ and append it to $B$.
- Remove $2$ from $A$ and push it into $S$.
- Remove $2$ from $S$ and append it to $B$.
- Remove $4$ from $A$ and push it into $S$.
- Remove $3$ from $A$ and push it to $S$.
- Remove $3$ from $S$ and append it to $B$.
- Remove $4$ from $S$ and append it to $B$.

By following above sequence of operations you end up with $B = [1, 2, 3, 4]$.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-22T01:38:56.548Z  

```py
# cook your dish here
from collections import deque
t=int(input())
for _ in range(t):
    n=int(input())
    a=deque(list(map(int,input().split())))
    stack=[]
    b=[]
    need=1
    for i in range(len(a)):
        stack.append(a.popleft())
        while stack and stack[-1]==need:
            b.append(stack.pop())
            need+=1
    if need==n+1:
        print("YES")
    else:
        print("NO")
        
```

---

[View on CodeChef](https://www.codechef.com/problems/STKSORT)