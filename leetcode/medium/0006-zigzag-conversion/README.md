# Zigzag Conversion

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

The string `"PAYPALISHIRING"` is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

```
P   A   H   N
A P L S I I G
Y   I   R

```

And then read line by line: `"PAHNAPLSIIGYIR"`

Write the code that will take a string and make this conversion given a number of rows:

```
string convert(string s, int numRows);

```

 

 **Example 1:** 

```
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

```

 **Example 2:** 

```
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I

```

 **Example 3:** 

```
Input: s = "A", numRows = 1
Output: "A"

```

 

 **Constraints:** 

- 1 <= s.length <= 1000
- s consists of English letters (lower-case and upper-case), ',' and '.'.
- 1 <= numRows <= 1000

## Solution

**Language:** Python  
**Runtime:** 7 ms (beats 91.42%)  
**Memory:** 12.5 MB (beats 21.97%)  
**Submitted:** 2026-10-11T14:07:21.021Z  

```py
class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [""] * numRows
        currRow = 0
        direction = -1

        for ch in s:
            rows[currRow] += ch

            if currRow == 0 or currRow == numRows - 1:
                direction *= -1

            currRow += direction

        return "".join(rows)
```

---

[View on LeetCode](https://leetcode.com/problems/zigzag-conversion/)