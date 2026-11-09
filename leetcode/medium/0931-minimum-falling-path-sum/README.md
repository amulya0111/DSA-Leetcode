# Minimum Falling Path Sum

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given an `n x n` array of integers `matrix`, return  *the  **minimum sum**  of any  **falling path**  through*  `matrix`.

A  **falling path**  starts at any element in the first row and chooses the element in the next row that is either directly below or diagonally left/right. Specifically, the next element from position `(row, col)` will be `(row + 1, col - 1)`, `(row + 1, col)`, or `(row + 1, col + 1)`.

 

 **Example 1:** 

```
Input: matrix = [[2,1,3],[6,5,4],[7,8,9]]
Output: 13
Explanation: There are two falling paths with a minimum sum as shown.

```

 **Example 2:** 

```
Input: matrix = [[-19,57],[-40,-5]]
Output: -59
Explanation: The falling path with a minimum sum is shown.

```

 

 **Constraints:** 

- n == matrix.length == matrix[i].length
- 1 <= n <= 100
- -100 <= matrix[i][j] <= 100

## Solution

**Language:** Python  
**Runtime:** 35 ms (beats 36.08%)  
**Memory:** 12.5 MB (beats 98.42%)  
**Submitted:** 2026-11-09T06:40:20.451Z  

```py
class Solution(object):
    def minFallingPathSum(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        m=len(matrix)
        n=len(matrix[0])
        # RECURSIVE:(BOTTOMUP)
        # def find(x,y,m,n):
        #     if x==m-1:
        #         return matrix[x][y]
        #     down=matrix[x][y]+find(x+1,y,m,n)
        #     dialeft=matrix[x][y]+(find(x+1,y-1,m,n) if y-1<0 else float('inf'))
        #     diaright=matrix[x][y]+(find(x+1,y+1,m,n) if y+1<n else float('inf'))
        #     return min(down,dialeft,diaright)
        # return find(0,0,m,n)

        # TABULATION:(TOPDOWN)
        dp=[[0]*n for _ in range(m)]
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if i==m-1:
                    dp[i][j]=matrix[i][j]
                    continue
                down=matrix[i][j]+(dp[i+1][j] if i+1<m else float('inf'))
                dialeft=matrix[i][j]+(dp[i+1][j-1] if i+1<m and j-1>=0 else float('inf'))
                diaright=matrix[i][j]+(dp[i+1][j+1] if i+1<m and j+1<n else float('inf'))
                dp[i][j]=min(down,dialeft,diaright)
        return min(dp[0][:])
```

---

[View on LeetCode](https://leetcode.com/problems/minimum-falling-path-sum/)