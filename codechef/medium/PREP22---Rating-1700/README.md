# PREP22 - Rating 1700

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Largest Rectangle in Histogram

You are given an array $A_1, A_2, \dots, A_N$ of length $N$. $A$ represents a histogram which means the height of the $i^{th}$ bar will be $A_i$ units and the width of each bar is $1$ unit.

Find the area of the largest rectangle in the histogram.

## Function Declaration
### Function Name

$largestRectangleArea$ – This function calculates the maximum rectangular area possible within the given histogram.

### Parameters

$N$ : An integer representing the number of bars in the histogram.
$A$ : An array of integers representing the heights of the histogram bars.

### Return Value

Returns an integer: the area of the largest rectangle that can be formed in the histogram.

### Constraints:

$1 \leq T \leq 10$
$1 \le N \le 10^5$
$0 \le A_i \le 10^9$

 *The input and output formats provided below are only for testing with custom inputs. You only need to return the value. Printing is handled automatically.* 

### Input Format
- The first line of input will contain a single integer $T$, denoting the number of test cases.
- The first line of each test case contains an integer $N$ - the length of the array $A$.
- The second line of each test case contains $N$ space-separated integers $A_1,A_2,\ldots,A_N$.
### Output Format

For each test case, output on a new line the area of the largest rectangle in the histogram.

### Subtasks
- Subtask 1 (30 points): $1 \leq N \leq 1000$
- Subtask 2 (70 points): No further constraints.
### Sample 1:
Input
Output

```
3
4
2 6 8 4
4
5 10 5 2
2
5 5

```

```
12
15
10

```

### Explanation:

 **Test case $1$** : Largest rectangle will create using $A_2$, $A_3$. So height will be $\min(6, 8) = 6$, width will be $2$. So area will be $12$.

 **Test case $2$** : Largest rectangle will create using $A_1$, $A_2$, $A_3$. So height will be $\min(5, 10, 5) = 5$, width will be $3$. So area will be $15$.

 **Test case $3$** : Largest rectangle will create using $A_1$, $A_2$. So height will be $\min(5, 5) = 5$, width will be $2$. So area will be $10$.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-17T03:37:09.239Z  

```py
def largestRectangleArea(N: int, A: list[int]) -> int:
    stack=[]
    area=0
    for i in range(N):
        while stack and A[i]<A[stack[-1]]:
            y=stack.pop()
            h=A[y]
            if stack:
                w=i-stack[-1]-1
            else:
                w=i
            area=max(area,h*w)
        stack.append(i)
        
    while stack:
        y=stack.pop()
        h=A[y]
        if stack:
            w=N-stack[-1]-1
        else:
            w=N 
        area=max(area,h*w)
    return area 
```

---

[View on CodeChef](https://www.codechef.com/problems/PREP22)