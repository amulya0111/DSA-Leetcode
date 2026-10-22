# PREP60 - Rating 1620

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Previous smaller element

You are given an array $A$ of size $N$.

We define the  *previous smaller element*  of an element $A_i$ as the element $A_j$ such that $A_j \lt A_i$ and $j$ is  **maximum**  possible.

Find the  *previous smaller element*  for every element $A_i$ in the array. Output $-1$ for the elements which have no  *previous smaller element*.

### Input Format
- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of multiple lines of input. The first line of each test case contains an integer - $N$. The next line contains $N$ space-separated integers - the array $A$.
### Output Format

For each test case, output on a new line, $N$ space-separated integers denoting the  *previous smaller element*  of the $i^{th}$ element of the array. Output $-1$ for the elements which have no  *previous smaller element*.

### Constraints
- $1 \leq T \leq 100$
- $1 \leq N \leq 10^5$
- $1 \leq A_i \leq 10^9$
- The sum of $N$ over all test cases won't exceed $2\times 10^5$.
### Sample 1:
Input
Output

```
3
5
4 5 2 10 8
3
3 2 1
4
1 2 3 4

```

```
-1 4 -1 2 2 
-1 -1 -1 
-1 1 2 3 

```

### Explanation:

 **Test case $1$:**  Given $A$ as $[4, 5, 2, 10, 8]$.

- $i=1$: No element to the left. Hence $-1$ is the output.
- $i=2$: The element at $i=1$ is smaller than that at $i=2$ and is at the nearest left. Hence $A_1=4$ is the output.
- $i=3$: No element to the left which is smaller than $A_3=2$. Hence $-1$ is the output.
- $i=4$: The element at $i=3$ is smaller than that at $i=4$ and is at the nearest left. Hence $A_3=2$ is the output.
- $i=5$: The element at $i=3$ is smaller than that at $i=5$ and is at the nearest left. Hence $A_3=2$ is the output.

 **Test case $2$:**  Given $A$ as $[3, 2, 1]$.

- $i=1$: No element to the left. Hence $-1$ is the output.
- $i=2$: No element to the left which is smaller than $2$. Hence $-1$ is the output.
- $i=3$: No element to the left which is smaller than $1$. Hence $-1$ is the output.

 **Test case $3$:**  Given $A$ as $[1, 2, 3, 4]$.

- $i=1$: No element to the left. Hence $-1$ is the output.
- $i=2$: The element at $i=1$ is smaller than that at $i=2$ and is at the nearest left. Hence $A_1=1$ is the output.
- $i=3$: The element at $i=2$ is smaller than that at $i=3$ and is at the nearest left.. Hence $A_2=2$ is the output.
- $i=4$: The element at $i=3$ is smaller than that at $i=4$ and is at the nearest left.. Hence $A_3=3$ is the output.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-22T02:09:16.596Z  

```py
# cook your dish here
t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    stack=[]
    ans=[None]*n
    for i in range(n):
        while stack and stack[-1]>a[i]:
            stack.pop()
        ans[i]=stack[-1] if stack else -1
        stack.append(a[i])
    print(" ".join(map(str,ans)))
    
```

---

[View on CodeChef](https://www.codechef.com/problems/PREP60)