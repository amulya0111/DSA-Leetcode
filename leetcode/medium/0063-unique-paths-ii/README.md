# Unique Paths II

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

You are given an `m x n` integer array `grid`. There is a robot initially located at the  **top-left corner**  (i.e., `grid[0][0]`). The robot tries to move to the  **bottom-right corner**  (i.e., `grid[m - 1][n - 1]`). The robot can only move either down or right at any point in time.

An obstacle and space are marked as `1` or `0` respectively in `grid`. A path that the robot takes cannot include  **any**  square that is an obstacle.

Return  *the number of possible unique paths that the robot can take to reach the bottom-right corner*.

The testcases are generated so that the answer will be less than or equal to `2 * 109`.

 

 **Example 1:** 

```
Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
Output: 2
Explanation: There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right

```

 **Example 2:** 

```
Input: obstacleGrid = [[0,1],[0,0]]
Output: 1

```

 

 **Constraints:** 

- m == obstacleGrid.length
- n == obstacleGrid[i].length
- 1 <= m, n <= 100
- obstacleGrid[i][j] is 0 or 1.

## Solution

**Language:** Python  
**Runtime:** 0 ms  
**Memory:** 12.2 MB  
**Submitted:** 2026-11-07T03:02:07.693Z  

```py
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        # RECURSIVE:(BOTTOM UP)
        # def find(x,y,m,n,grid):
        #     if x==m-1 and y==m-1:
        #         return 1
        #     if x>m-1 or y>n-1 or grid[x][y]==1:
        #         return 0
        #     right=find(x,y+1,m,n,grid)
        #     down=find(x+1,y,m,n,grid)
        #     return right+down     
        # return find(0,0,m,n,obstacleGrid)

        # TABULATION:(TOP DOWN)
        if obstacleGrid[m-1][n-1]==1 or obstacleGrid[0][0]==1:
            return 0
        dp=[[1]*n for i in range(m)]
        for i in range(m-2,-1,-1):
            for j in range(n-2,-1,-1):
                right=dp[i][j+1] if obstacleGrid[i][j+1]==0 else 0
                down = dp[i+1][j] if obstacleGrid[i+1][j]==0 else 0
                dp[i][j]=right+down
        return dp[0][0]           

```

---

[View on LeetCode](https://leetcode.com/problems/unique-paths-ii/)