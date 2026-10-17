# MXWATR - Rating 1700

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Maximum water in a section

Chef owns a swimming pool with width $N$ meters which contains $N$ continuous walls with height $h_i$ (possible zero) and width $1$ meter each.

When it rains heavily, water is stored in the swimming pool in the form of sections (check Figure 1). Chef is busy calling his friends for a party. So, you need to determine the maximum water stored in  **a section**  among all the sections after a heavy rain.

Figure 1 :

This swimming pool has 3 sections :

- Section 2 has the maximum water i.e 10 units.
- Section 1 has 9 units of water.
- Section 3 contains 2 units of water.

So, the answer would be 10 units (maximum of all the sections)

### Input Format
- First line will contain $T$, number of testcases. Then the testcases follow.
- First line of each testcase contains an integer $N$ - number of walls $A$.
- Second line contains N space separated integers $h_1, h_2,....., h_N$
### Output Format

For each testcase, output one integer in a single line - Maximum water stored among all sections.

### Constraints
- $1 \leq T \leq 10^3$
- $2 \leq N \leq 10^5$
- $0 \leq h_i \leq 10^6$

Sum of $N$ over all test cases will not exceed $10^5$

### Subtasks
- 30 points : $2 \leq N \leq 500, \sum N_i \leq 500$
- 70 points : Original Constraints
### Sample 1:
Input
Output

```
2
4
5 0 2 6
6
3 1 4 0 3 5 
```

```
8
5
```

### Explanation:

 **Test Case 1**  : ![Test Case 1](https://s3.amazonaws.com/codechef_shared/download/Images/Aman/Copy+of+Test+Case+1.png =200x300)

This swimming pool has only 1 section with 8 units of water.

 **Test Case 2**  : ![Test Case 2](https://s3.amazonaws.com/codechef_shared/download/Images/Aman/Copy+of+Test+Case+2.png =300x300)

This swimming pool has 2 sections :

- Section 1 has 2 units of water.
- Section 2 has maximum water i.e 5 units.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-17T04:34:43.772Z  

```py
# cook your dish here
t=int(input())
for _ in range(t):
    n=int(input())
    height=list(map(int,input().split()))
    stack=[]
    water=0
    curr=0
    for i in range(n):
        if stack and height[i] > height[stack[0]]:
            water = max(water, curr)
            curr = 0
            stack = []
        while stack and height[i]>=height[stack[-1]]:
            y=stack.pop()
            
            if not stack:
                break
            
            h=min(height[i],height[stack[-1]])-height[y]
            w=i-stack[-1]-1
            curr+=h*w
        stack.append(i)
    water=max(water,curr)
    print(water)
```

---

[View on CodeChef](https://www.codechef.com/problems/MXWATR)