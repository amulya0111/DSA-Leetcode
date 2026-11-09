# NPTAS01

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Chef Finds Falling Path

Chef has found a square matrix filled with integers and wants to find a special path through it. This path, called a falling path, starts from any element in the first row and moves downwards row by row.
At each step, Chef can move to the element directly below or diagonally adjacent (left or right) in the next row. Chef wants to calculate the minimum possible sum of the elements along such a falling path from the top row to the bottom row.
Help Chef by writing a function that computes this minimum sum efficiently.

## Function Declaration
### Function Name

$calculateMinFallingPathSum$

### Parameters
- $inputMatrix$ : A 2D square matrix representing the grid of integers. The dimensions of the matrix are rowCount x columnCount, where rowCount == columnCount.
### Return Value
- Returns an integer representing the minimum sum achievable from a falling path through the matrix.
## Constraints
- $1 \leq T \leq 10$
- $1 \leq n = \text{rowCount} = \text{columnCount} \leq 100$
- $-100 \leq \text{inputMatrix}[i][j] \leq 100$ for $0 \leq i, j < n$

 **The input and output formats given below are only if you want to test using custom inputs.** 

### Input Format
## Input Format
- The first line contains a single integer $T$ — the number of test cases.
- For each test case: The first line contains an integer $n$ — the size of the square matrix. The next $n$ lines each contain $n$ space-separated integers representing the rows of Chef's matrix.
### Output Format
- For each test case, print a single integer — the minimum sum of any falling path through Chef's matrix.
- The input and output formats given below are only if you want to test using custom inputs.
### Sample 1:
Input
Output

```
2
3
[1 2 3]
[4 5 6]
[7 8 9]
4
[10 10 10 10]
[5 5 5 5]
[1 1 1 1]
[0 0 0 0]
```

```
12
16
```

### Explanation:
- For the first test case, the minimum falling path is 1 -> 4 -> 7, summing to 12.
- For the second test case, the minimum path is 10 -> 5 -> 1 -> 0, totaling 16.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-11-09T06:59:16.546Z  

```py
class Solution:
    def calculateMinFallingPathSum(self, matrix):
        # write your code here
        m=len(matrix)
        n=len(matrix[0])
        dp=[0]*n
        for i in range(m-1,-1,-1):
            prev=dp[:]
            for j in range(n-1,-1,-1):
                if i==m-1:
                    dp[j]=matrix[i][j]
                    continue
                down=matrix[i][j] + prev[j]
                dialeft=matrix[i][j] + (prev[j-1] if j-1>=0 else float('inf'))
                diaright=matrix[i][j] + (prev[j+1] if j+1<m else float('inf'))
                dp[j]=min(down,dialeft,diaright)
        return min(dp)
```

---

[View on CodeChef](https://www.codechef.com/problems/NPTAS01)