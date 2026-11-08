# ZJIHK01 - Rating 1150

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Chef Counts Unique Paths

Chef has a robot that starts at the top-left corner of a grid and wants to reach the bottom-right corner. The grid contains some obstacles, marked as 1, while free spaces are marked as 0.
Chef’s robot can only move either down or right at any point in time. Chef wants to know how many unique paths exist from start to finish without passing through any obstacles.
Help Chef calculate the total number of such valid paths.

## Function Declaration
### Function Name

$countUniquePaths$ - This function calculates the number of unique paths from the top-left to the bottom-right corner of a grid, considering obstacles.

### Parameters
- $grid$ : A 2D grid where each cell is either 0 (free space) or 1 (obstacle).
- The grid dimensions can vary, and the function must handle grids with obstacles blocking the path.
### Return Value
- Returns a number representing the total number of unique paths from start to finish.
- The output counts only valid paths that do not pass through obstacles.
- If path starts with an obstacle then there is no path that exists.
- If no path exists, the function returns 0.
## Constraints
- $1 \leq T \leq 100$
- Let $n$ be the number of rows in $grid$.
- $1 \leq n \leq 100$
- Each element in $grid$ is either 0 or 1.
- $Rows*Column \leq 300$
- The answer will be less than or equal to $2 \times 10^9$.
- The $grid$ may or may not be a square.

 **The input and output formats given below are only if you want to test using custom inputs.** 

### Input Format
- The first line contains $T$ number of test cases.
- The first line contains $n$ — the number of rows of the grid.
- The next $n$ lines each contain integers (0 or 1) representing the grid.
### Output Format
- Print a single number — the total number of unique paths Chef’s robot can take from the top-left corner to the bottom-right corner without crossing any obstacles.
- If no such path exists, print 0.
### Sample 1:
Input
Output

```
2
3
[0 0 1]
[0 0 0]
[1 0 0]
4
[0 1 0 0]
[0 0 1 0]
[1 0 0 0]
[0 0 0 0]
```

```
4
3
```

### Explanation:
- For the first test case, four paths avoid obstacles (cells with 1) by moving right, down, down, right.
- In the second test case, three distinct paths navigate around obstacles to reach the bottom-right corner.
### Sample 2:
Input
Output

```
1
2
[0 0]
[0 0]
```

```
2
```

### Explanation:
- For the 2x2 grid with no obstacles, there are 2 ways to reach the bottom-right corner: right then down, or down then right.
### Sample 3:
Input
Output

```
1
5
[0 0 0 0 0]
[0 1 1 1 0]
[0 1 0 1 0]
[0 1 0 0 0]
[0 0 0 1 0]
```

```
1
```

### Explanation:
- The grid blocks paths with 1s; only 1 ways avoid obstacles from top-left to bottom-right by moving around them.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-11-08T17:08:06.845Z  

```py
class Solution:
    def countUniquePaths(self, grid):
        # write your code here
        m=len(grid)
        n=len(grid[0])
        if grid[0][0]==1 or grid[m-1][n-1]==1:
            return 0
        dp=[0]*n
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if i==m-1 and j==n-1:
                    dp[n-1]=1
                    continue
                if grid[i][j]==1:
                    dp[j]=0
                    continue
                right=dp[j+1] if j+1<n else 0
                down=dp[j] if i+1<m else 0
                dp[j]=right+down
        return dp[0]
```

---

[View on CodeChef](https://www.codechef.com/problems/ZJIHK01)