# BGJOM01 - Rating 1250

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Chef Finds Minimum Path

Chef has a grid $grid$ filled with non-negative numbers and wants to find a path from the top-left corner to the bottom-right corner that minimizes the sum of all numbers along the path.
Chef can only move either down or right at any point in time. Help Chef determine the minimum possible sum for such a path.

## Function Declaration
### Function Name

$calculateMinimumPathSum$ - This function calculates the minimum path sum from the top-left to the bottom-right corner of a grid by moving only down or right.

### Parameters
- $grid$ : A 2D matrix representing the grid of non-negative integers.
- Each element in $numberGrid$ represents the cost or value at that grid cell.
### Return Value
- Returns a number representing the minimum sum path value.
- The return value is the smallest sum of numbers along a path from the top-left to bottom-right cell.
- The path can only move either down or right at any point in time.
## Constraints
- $1 \leq T \leq 10$
- $1 \leq rowCount \leq 200$
- $0 \leq numberGrid[i][j] \leq 200$
- The $grid$ can be either rectangle or square.
### Input Format
- First line contains the $T$ - test cases.
- The first line contains $rowCount$ — the number rows in Chef's grid.
- The next $rowCount$ lines each contain integers representing the values in $grid$.
### Output Format
- Print a single integer — the minimum sum of numbers along a path from the top-left to the bottom-right corner of the grid, moving only down or right.
### Sample 1:
Input
Output

```
2
2
[1 2 3]
[4 5 6]
3
[10 1 10]
[1 10 1]
[10 1 10]
```

```
12
32
```

### Explanation:
- For the first test case, the minimum path is 1 -> 2 -> 3 -> 6 with sum 12.
- For the second test case, the minimum path is 10 -> 1 -> 10 -> 1 -> 10 with sum 32.
### Sample 2:
Input
Output

```
2
2
[0 0]
[0 0]
3
[7 2 3]
[1 0 4]
[2 1 0]
```

```
0
9
```

### Explanation:
- For the first test case, all values are zero, so the minimum path sum from top-left to bottom-right is 0.
- In the second test case, the minimum path is 7 -> 1 -> 0 -> 1 -> 0, summing up to 9.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-11-09T05:47:26.005Z  

```py
class Solution:
    def calculateMinimumPathSum(self, grid):
        # write your code here 
        m=len(grid)
        n=len(grid[0])
        dp=[0]*n
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if i==m-1 and j==n-1:
                    dp[j]=grid[i][j]
                    continue
                right=grid[i][j] + (dp[j+1] if j+1<n else float('inf'))
                down=grid[i][j] + (dp[j] if i+1<m else float('inf'))
                dp[j]=min(right,down)
        return dp[0]
```

---

[View on CodeChef](https://www.codechef.com/problems/BGJOM01)