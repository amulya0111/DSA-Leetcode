# Minimum Path Sum

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given a `m x n` `grid` filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

 **Note:**  You can only move either down or right at any point in time.

 

 **Example 1:** 

```
Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.

```

 **Example 2:** 

```
Input: grid = [[1,2,3],[4,5,6]]
Output: 12

```

 

 **Constraints:** 

- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 200
- 0 <= grid[i][j] <= 200

## Solution

**Language:** Python  
**Runtime:** 20 ms (beats 18.11%)  
**Memory:** 12.8 MB (beats 90.58%)  
**Submitted:** 2026-11-09T05:37:31.115Z  

```py
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m=len(grid)
        n=len(grid[0])
        # RECURSIVE:(BOTTOMUP)
        # def find(x,y,m,n):
        #     if x==m or y==n:
        #         return float('inf')
        #     if x==m-1 and y==n-1:
        #         return grid[x][y]
        #     right=grid[x][y]+find(x,y+1,m,n)
        #     down=grid[x][y]+find(x+1,y,m,n)
        #     return min(right,down)
        # return find(0,0,m,n)

        # TABULATION:(TOPDOWN)
        # dp=[[0]*n for i in range(m)]
        # for i in range(m-1,-1,-1):
        #     for j in range(n-1,-1,-1):
        #         if i==m-1 and j==n-1:
        #             dp[i][j]=grid[i][j]
        #             # it doesnt have right or down so continue
        #             continue
        #         right=grid[i][j]+(dp[i][j+1] if j+1<n else float('inf'))
        #         down=grid[i][j]+(dp[i+1][j]  if i+1<m else float('inf'))
        #         dp[i][j]=min(right,down)
        # return dp[0][0]

        # SINGLE-ARRAY:(TOP DOWN)
        dp=[0]*n
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if i==m-1 and j==n-1:
                    dp[j]=grid[i][j]
                    continue
                right=grid[i][j]+(dp[j+1] if j+1 < n else float('inf'))
                down=grid[i][j]+(dp[j] if i+1 < m else float('inf'))
                dp[j]=min(right,down)
        return dp[0]
```

---

[View on LeetCode](https://leetcode.com/problems/minimum-path-sum/)