# Count Unique Characters of All Substrings of a Given String

![Difficulty](https://img.shields.io/badge/Difficulty-Hard-red)

## Problem

Let's define a function `countUniqueChars(s)` that returns the number of unique characters in `s`.

- For example, calling countUniqueChars(s) if s = "LEETCODE" then "L", "T", "C", "O", "D" are the unique characters since they appear only once in s, therefore countUniqueChars(s) = 5.

Given a string `s`, return the sum of `countUniqueChars(t)` where `t` is a substring of `s`. The test cases are generated such that the answer fits in a 32-bit integer.

Notice that some substrings can be repeated so in this case you have to count the repeated ones too.

 

 **Example 1:** 

```
Input: s = "ABC"
Output: 10
Explanation: All possible substrings are: "A","B","C","AB","BC" and "ABC".
Every substring is composed with only unique letters.
Sum of lengths of all substring is 1 + 1 + 1 + 2 + 2 + 3 = 10

```

 **Example 2:** 

```
Input: s = "ABA"
Output: 8
Explanation: The same as example 1, except countUniqueChars("ABA") = 1.

```

 **Example 3:** 

```
Input: s = "LEETCODE"
Output: 92

```

 

 **Constraints:** 

- 1 <= s.length <= 105
- s consists of uppercase English letters only.

## Solution

**Language:** Python  
**Runtime:** 233 ms (beats 20.45%)  
**Memory:** 15.8 MB (beats 52.27%)  
**Submitted:** 2026-10-28T17:25:05.313Z  

```py
class Solution(object):
    def uniqueLetterString(self, s):
        n = len(s)
        last = {}
        prev = {}
        ans = 0

        for i in range(n):
            ch = s[i]

            p = last.get(ch, -1)
            q = prev.get(ch, -1)

            ans += (i - p) * (p - q)

            prev[ch] = p
            last[ch] = i

        for ch in last:
            ans += (n - last[ch]) * (last[ch] - prev[ch])

        return ans
```

---

[View on LeetCode](https://leetcode.com/problems/count-unique-characters-of-all-substrings-of-a-given-string/)