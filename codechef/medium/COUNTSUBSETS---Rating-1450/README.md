# COUNTSUBSETS - Rating 1450

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Count subsets with sum K

You are given an array of integers and a target value $K$. Your task is to determine how many  **distinct subsets**  of the array have a total sum exactly equal to $K$.

A subset can include or exclude any element of the array, but each element can be used  **at most once**. If the array contains duplicate values, subsets formed using different positions are considered  **different**.

Since the answer can be large, return the count modulo $10^9 + 7$.

## Function Declaration
### Function Name

$countSubsetsWithSumK$ – This function counts the number of subsets whose sum is exactly equal to a given target value.

### Parameters
- $n$ : The number of elements in the array.
- $K$ : The target sum.
- $arr$ : An array of integers of size $n$.
### Return Value
- Returns an integer representing the number of subsets whose sum equals $K$, taken modulo $10^9 + 7$.
## Constraints
- $1 \leq T \leq 10$
- $1 \leq n \leq 100$
- $1 \leq arr[i] \leq 10^3$
- $1 \leq K \leq 10^3$
### Input Format
- The first line contains a single integer T — the number of test cases.
- For each test case: The first line contains two integers n and K — the size of the array and the target sum. The second line contains n space-separated integers representing the array arr.
### Output Format
- For each test case, print a single integer — the number of subsets whose sum is exactly K.
### Sample 1:
Input
Output

```
1
5 7
1 2 3 4 5
```

```
3
```

### Explanation:

Valid subsets are:

- [2, 5]
- [3, 4]
- [1, 2, 4]
### Sample 2:
Input
Output

```
1
4 6
3 3 3 3

```

```
6
```

### Explanation:

Any pair of `3`s forms a valid subset. Number of ways to choose 2 elements from 4 is ($\binom{4}{2} = 6$).

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-11-10T06:29:19.371Z  

```py
mod=10**9+7
class Solution:
    def countSubsetsWithSumK(self, n, K, arr):
        # write your code here 
        dp=[0]*(K+1)
        dp[0]=1
        for i in range(n):
            for j in range(K,arr[i]-1,-1):
                dp[j]+= dp[j-arr[i]]
        return dp[K]%mod
```

---

[View on CodeChef](https://www.codechef.com/problems/COUNTSUBSETS)