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
**Submitted:** 2026-10-20T03:55:46.753Z  

```py
# cook your dish here
t = int(input())

def max_vol(arr):
    if len(arr) < 3:
        return 0
    max_height = 0
    cur_vol = 0
    max_v = 0
    for h in arr:
        if h >= max_height:
            max_height = h 
            max_v = max(max_v, cur_vol)
            cur_vol = 0 
        else:
            cur_vol += max_height - h
    return max_v

for _ in range(t):
    n = int(input())
    height = list(map(int, input().split()))
    
    h_max = max(height)
    h_max_ind = height.index(h_max)
    
    h_left = height[:h_max_ind + 1]
    h_right = height[h_max_ind:]
    h_right.reverse()
    
    max_left = max_vol(h_left)
    max_right = max_vol(h_right)
    
    print(max(max_left, max_right))
```

---

[View on CodeChef](https://www.codechef.com/problems/MXWATR)