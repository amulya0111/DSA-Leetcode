# EIHKO01 - Rating 1150

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Chef Counts Unique Paths

Chef has a robot placed on a grid with dimensions $rowCount \times columnCount$. The robot starts at the top-left corner of the grid and wants to reach the bottom-right corner.
However, the robot can only move either one step down or one step right at any time. Chef wants to find out how many unique paths the robot can take to reach its destination.
Help Chef calculate the total number of such unique paths.

## Function Declaration
### Function Name

$calculateUniquePaths$ - This function computes the number of unique paths from the top-left corner to the bottom-right corner of a grid.

### Parameters
- $rowCount$ : The number of rows in the grid, representing the vertical dimension.
- $columnCount$ : The number of columns in the grid, representing the horizontal dimension.
### Return Value
- Returns a number representing the total count of unique paths.
- The return value indicates how many distinct ways exist to move only down or right to reach the grid's bottom-right cell.
## Constraints
- $1 \leq T \leq 100$
- $1 \leq rowCount, columnCount \leq 100$
- $rowCount*columnCount \leq 300$
- The answer for each test case will be less than or equal to $2 \times 10^9$.
### Input Format
- The first line contains a single integer $T$ — the number of test cases.
- Each of the next $T$ lines contains two integers $rowCount$ and $columnCount$ separated by a space, representing the dimensions of the grid.
### Output Format
- For each test case, print a single line containing the number of unique paths the robot can take to reach the bottom-right corner of the grid.
### Sample 1:
Input
Output

```
3
1 1
2 2
10 10
```

```
1
2
48620
```

### Explanation:
- For 1 1: There's only one cell, so only 1 path.
- For 2 2: Paths = C(2,1) = 2 ways to move right or down.
- For 10 10: Paths = C(18,9) = 48620 ways using combinations formula.
### Sample 2:
Input
Output

```
4
5 5
3 4
4 3
7 8
```

```
70
10
10
1716
```

### Explanation:
- t=1: Paths from top-left to bottom-right in 5x5 grid = C(8,4) = 70.
- t=2: Paths in 3x4 grid = C(5,2) = 10.
- t=3: Paths in 4x3 grid = C(5,2) = 10.
- t=4: Paths in 7x8 grid = C(13,7) = 1716.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-11-04T18:23:01.338Z  

```py
class Solution:
    def calculateUniquePaths(self, rowCount, columnCount):
        # write your code here 
        # write your code here
        dp=[1]*columnCount
        for i in range(rowCount-2,-1,-1):
            for j in range(columnCount-2,-1,-1):
                dp[j]=dp[j]+dp[j+1]
        return dp[0]
```

---

[View on CodeChef](https://www.codechef.com/problems/EIHKO01)