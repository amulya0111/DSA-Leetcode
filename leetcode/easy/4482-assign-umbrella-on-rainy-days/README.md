# Q1. Assign Umbrella on Rainy Days

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

You are given a  **binary array**  `rain` of length `n`, where `rain[i] == 1` means it rains on day `i`, and `rain[i] == 0` means it does not.

Alice and Bob share a  **single umbrella**  over these `n` days. On each day `i`:

- Alice needs the umbrella on day i if rain[i] == rain[i + 1] == 1 for 0 <= i < n - 1.
- Bob needs the umbrella if rain[i] == 1.
- At most one of them can receive the umbrella.
- If only one person needs it, that person receives it.
- If both need it, it goes to whoever has received it fewer times so far. If they are tied, it goes to Alice.
- If neither needs it, no one receives it.

A person's count  **increases**  only on a day they receive the umbrella. Initially, both counts are 0.

Return a string array `answer` of length `n`, where `answer[i]` is `"Alice"`, `"Bob"`, or `"None"`, denoting who receives the umbrella on day `i`.

A  **binary array**  is an array that contains only 0 and 1.

 

Original
Python
 **Example 1:** 

 **Input:**  rain = [1,1,0,1,1]

 **Output:**  ["Alice","Bob","None","Alice","Bob"]

 **Explanation:** 

- Day 0: rain[0] == 1 and rain[1] == 1, so both need it. Counts are tied, so Alice receives it.
- Day 1: rain[1] == 1, so Bob needs it, but rain[2] == 0, so Alice does not need it. Therefore Bob receives it.
- Day 2: No rain, so no one receives it.
- Day 3: rain[3] == 1 and rain[4] == 1, so both need it. Counts are tied at 1, so Alice receives it.
- Day 4: Last day, so only Bob needs it, and he receives it.
- Therefore, answer = ["Alice", "Bob", "None", "Alice", "Bob"].

 **Example 2:** 

 **Input:**  rain = [0,1,0,1]

 **Output:**  ["None","Bob","None","Bob"]

 **Explanation:** 

- It never rains on two consecutive days, so Alice never needs the umbrella.
- Bob receives it on days 1 and 3, and no one receives it on days 0 and 2.
- Therefore, answer = ["None", "Bob", "None", "Bob"].

 

 **Constraints:** 

- 1 <= n == rain.length <= 100
- rain[i] is either 0 or 1.

## Solution

**Language:** Python  
**Runtime:** 7 ms (beats 100.00%)  
**Memory:** 12.1 MB (beats 100.00%)  
**Submitted:** 2026-11-21T15:08:49.350Z  

```py
class Solution(object):
    def assignUmbrella(self, rain):
        """
        :type rain: List[int]
        :rtype: List[str]
        """
        ans=[]
        n=len(rain)
        a="Alice"
        b="Bob"
        e="None"
        ac=0
        bc=0
        for i in range(n):
            if i==n-1 and rain[i]==1:
                ans.append(b)
                break
            if rain[i]==1:
                if rain[i+1]==1:
                    if ac<=bc:
                        ans.append(a)
                        ac+=1
                    else:
                        ans.append(b)
                        bc+=1
                else:
                    ans.append(b)
                    bc+=1
            else:
                ans.append(e)
        return ans
```

---

[View on LeetCode](https://leetcode.com/problems/assign-umbrella-on-rainy-days/)