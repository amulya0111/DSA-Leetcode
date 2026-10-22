# Longest Valid Parentheses

![Difficulty](https://img.shields.io/badge/Difficulty-Hard-red)

## Problem

Given a string containing just the characters `'('` and `')'`, return  *the length of the longest valid (well-formed) parentheses **substring*.

 

 **Example 1:** 

```
Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".

```

 **Example 2:** 

```
Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".

```

 **Example 3:** 

```
Input: s = ""
Output: 0

```

 

 **Constraints:** 

- 0 <= s.length <= 3 * 104
- s[i] is '(', or ')'.

## Solution

**Language:** Python  
**Runtime:** 23 ms (beats 36.68%)  
**Memory:** 13.6 MB (beats 36.99%)  
**Submitted:** 2026-10-22T02:34:06.482Z  

```py
class Solution(object):
    def longestValidParentheses(self, s):
        n = len(s)
        stack = [-1]
        ans = 0

        for i in range(n):
            if s[i] == "(":
                stack.append(i)
            else:
                stack.pop()

                if not stack:
                    stack.append(i)
                else:
                    ans = max(ans, i - stack[-1])

        return ans
```

---

[View on LeetCode](https://leetcode.com/problems/longest-valid-parentheses/)