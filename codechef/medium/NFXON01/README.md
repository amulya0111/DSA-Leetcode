# NFXON01

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Chef Circular Search

Chef has a  **circular list of integers**  and wants to find the  **next strictly greater element**  for every number in the list.

- Since the list is circular, after reaching the end, Chef continues searching from the beginning.
- For each number, Chef wants the first strictly greater element found while moving forward.
- If no greater number exists, record $-1$.

Help Chef efficiently find the next strictly greater element for every item in his circular list!

## Function Declaration
- Function Name $findNextGreaterElements$
- Parameters $numbers$: a list of integers representing the circular list
- Return Value An array of integers where each position contains the next greater element of the corresponding item in $numbers$, or $-1$ if none exists.
## Constraints
- $1 \leq T \leq 100$
- $1 \leq N \leq 10^4$
- $-10^9 \leq numbers[i] \leq 10^9$
### Input Format
- The first line contains a single integer $T$ — the number of test cases.
- For each test case: The first line contains an integer $N$ — the size of $numbers$. The second line contains $N$ integers representing $numbers$.
### Output Format
- For each test case, print $N$ integers in one line.
- Each integer represents the next greater element for the corresponding number in $numbers$, or $-1$ if no such element exists.
### Sample 1:
Input
Output

```
2
3
4 1 2
5
5 4 3 2 1
```

```
-1 2 4
-1 5 5 5 5
```

### Explanation:
- $4$: Numbers after $4$ in the circular list are [1, 2]. None are greater, so the result is $-1$
- $1$: Numbers after $1$ are [2, 4]. The first greater number is $2$
- $2$: Numbers after $2$ are [4, 1]. The first greater number is $4$

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-14T16:29:47.379Z  

```py
def findNextGreaterElements(numbers):
    stack=[]
    n=len(numbers)
    ans=[-1]*n
    for i in range(0,n):
        while stack and numbers[stack[-1]]<=numbers[i]:
            idx=stack.pop()
            ans[idx]=numbers[i] 
        stack.append(i)
    for i in range(n-1,-1,-1):\
        while stack and numbers[stack[-1]]<=numbers[i]:
            idx=stack.pop()
            ans[idx]=numbers[i] 
        
    return ans
        
```

---

[View on CodeChef](https://www.codechef.com/problems/NFXON01)