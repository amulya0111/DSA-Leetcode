# Q1. Count Valid Substrings I

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

You are given a string `s` consisting only of the characters `'a'`, `'b'`, and `'c'`.

A string is called  **valid**  if it does not contain `"abc"` as a  **substring**.

Return the number of  **valid substrings**  in `s`. Substrings with different starting or ending indices are counted separately.

A  **substring**  is a contiguous  **non-empty**  sequence of characters within a string.

 

 **Example 1:** 

 **Input:**  s = "abac"

 **Output:**  10

 **Explanation:** 

The following substrings don't contain `"abc"`​​​​​​​ as a substring:

- s[0..0] = "a"
- s[0..1] = "ab"
- s[0..2] = "aba"
- s[0..3] = "abac"​​​​​​​
- s[1..1] = "b"
- s[1..2] = "ba"
- s[1..3] = "bac"
- s[2..2] = "a"
- s[2..3] = "ac"
- s[3..3] = "c"

Thus, the answer is 10.

 **Example 2:** 

 **Input:**  s = "abc"

 **Output:**  5

 **Explanation:** 

The following substrings don't contain `"abc"`​​​​​​​ as a substring:

- s[0..0] = "a"
- s[0..1] = "ab"
- s[1..1] = "b"
- s[1..2] = "bc"
- s[2..2] = "c"​​​​​​​

Thus, the answer is 5.

 **Example 3:** 

 **Input:**  s = "ac"

 **Output:**  3

 **Explanation:** 

All substrings in `s` don't contain `"abc"` as a substring​​​​​​​. Thus, the answer is 3.

 

 **Constraints:** 

- 1 <= s.length <= 105​​​​​​​
- s only consists of 'a', 'b', and 'c' characters.

## Solution

**Language:** Python  
**Runtime:** 277 ms (beats 100.00%)  
**Memory:** 16.4 MB (beats 100.00%)  
**Submitted:** 2026-11-07T15:25:33.245Z  

```py
class Solution(object):
    def countValidSubstrings(self, s):
        res=left=0
        for i in range(len(s)):
            if i>=2 and s[i-2:i+1]=="abc":
                left=i-1
            res+=i-left+1
        return res
```

---

[View on LeetCode](https://leetcode.com/problems/count-valid-substrings-i/)