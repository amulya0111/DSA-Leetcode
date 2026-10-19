# Maximal Rectangle

![Difficulty](https://img.shields.io/badge/Difficulty-Hard-red)

## Problem

Given a `rows x cols` binary `matrix` filled with `0`'s and `1`'s, find the largest rectangle containing only `1`'s and return  *its area*.

 

 **Example 1:** 

```
Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 6
Explanation: The maximal rectangle is shown in the above picture.

```

 **Example 2:** 

```
Input: matrix = [["0"]]
Output: 0

```

 **Example 3:** 

```
Input: matrix = [["1"]]
Output: 1

```

 

 **Constraints:** 

- rows == matrix.length
- cols == matrix[i].length
- 1 <= rows, cols <= 200
- matrix[i][j] is '0' or '1'.

## Solution

**Language:** Python  
**Runtime:** 70 ms (beats 49.30%)  
**Memory:** 17.8 MB (beats 98.66%)  
**Submitted:** 2026-10-19T16:16:01.910Z  

```py

class Solution(object):
    def maximalRectangle(self, matrix):
        if not matrix:
            return 0

        row = len(matrix)
        col = len(matrix[0])
        heights = [0] * col
        ans = 0

        for i in range(row):
            for j in range(col):
                if matrix[i][j] == "1":
                    heights[j] += 1
                else:
                    heights[j] = 0

            stack = []
            for j in range(col + 1):
                curr = heights[j] if j < col else 0

                while stack and heights[stack[-1]] > curr:
                    h = heights[stack.pop()]

                    if stack:
                        w = j - stack[-1] - 1
                    else:
                        w = j

                    ans = max(ans, h * w)

                stack.append(j)

        return ans

```

---

[View on LeetCode](https://leetcode.com/problems/maximal-rectangle/)