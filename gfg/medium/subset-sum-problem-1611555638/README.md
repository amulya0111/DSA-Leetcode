# Subset Sum Problem

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given an array of positive integers  **arr[]**  and a value  **sum**, find if there is a subset of arr[] with sum equal to given sum. 

 **Examples:** 

```
Input: arr[] = [3, 34, 4, 12, 5, 2], sum = 9
Output: true 
Explanation: Here there exists a subset with target sum = 9, 4+3+2 = 9.

```

```
Input: arr[] = [3, 34, 4, 12, 5, 2], sum = 30
Output: false
Explanation: There is no subset with target sum 30.
```

```
Input: arr[] = [1, 2, 3], sum = 6
Output: true
Explanation: The entire array can be taken as a subset, giving 1 + 2 + 3 = 6.
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-29T16:43:54.388Z  

```py
class Solution:
    def isSubsetSum(self, arr: list[int], sum: int) -> bool:
        # code here
        n=len(arr)
        k=sum
        dp=[[False]*(k+1) for _ in range(n)]
        for i in range(n):
            dp[i][0]=True
        # defining l=the last element we captured during memoization , if the value is < main target just add
        if arr[0]<=k:
            dp[0][arr[0]]=True
        for i in range(1,n):
            for target in range(1,k+1):
                # first not take 
                not_take=dp[i-1][target]
                take=False
                if arr[i]<=target:
                    take=dp[i-1][target-arr[i]]
                dp[i][target]=take or not_take
        return dp[n-1][k]
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/subset-sum-problem-1611555638/1)