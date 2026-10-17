# Trapping Rain Water

![Difficulty](https://img.shields.io/badge/Difficulty-Hard-red)

## Problem

Given `n` non-negative integers representing an elevation map where the width of each bar is `1`, compute how much water it can trap after raining.

 

 **Example 1:** 

```
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

```

 **Example 2:** 

```
Input: height = [4,2,0,3,2,5]
Output: 9

```

 

 **Constraints:** 

- n == height.length
- 1 <= n <= 2 * 104
- 0 <= height[i] <= 105

## Solution

**Language:** Python  
**Runtime:** 13 ms (beats 37.71%)  
**Memory:** 13.6 MB (beats 18.38%)  
**Submitted:** 2026-10-17T03:58:48.233Z  

```py
class Solution(object):
    def trap(self, height):
        stack = []
        water = 0
        n = len(height)

        for i in range(n):
            while stack and height[i] > height[stack[-1]]:
                y = stack.pop()

                if not stack:
                    break

                h = min(height[i], height[stack[-1]]) - height[y]
                w = i - stack[-1] - 1

                water += h * w

            stack.append(i)

        return water

```

---

[View on LeetCode](https://leetcode.com/problems/trapping-rain-water/)