# SUBSETTARGET - Rating 1350

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Subset with target sum

You are given an array of positive integers and a target value. Your task is to determine whether it is possible to select  **any subset**  of the given array such that the  **sum of the chosen elements is exactly equal to the target**.

Each element in the array can be used  **at most once**, and the subset does  **not need to be contiguous**.

## Function Declaration
### Function Name

$isSubsetSum$ – This function checks whether there exists a subset of the given array whose elements sum up exactly to the given target value.

### Parameters
- $n$ : The number of elements in the array.
- $arr$ : An array of integers representing the elements available.
- $target$ : The target sum to be achieved using a subset of the array.
### Return Value
- Returns $true$ if there exists at least one subset whose sum equals $target$.
- Returns $false$ otherwise.
## Constraints
- $1 \leq T \leq 10$
- $1 \leq n \leq 100$
- $1 \leq arr[i] \leq 100$
- $0 \leq target \leq 5000$
### Input Format
- The first line contains a single integer $T$ — the number of test cases.
- For each test case: The first line contains two integers $n$ and $target$, the size of the array and target sum. The second line contains $n$ space-separated integers representing the array $arr$.
### Output Format
- For each test case, print $true$ if a subset with sum equal to $target$ exists, otherwise print $false$.
- The input and output formats given below are only if you want to test using custom inputs.
### Sample 1:
Input
Output

```
1
4 9
3 8 4 5
```

```
true
```

### Explanation:
- A subset {4,5} exists whose sum is 9.
### Sample 2:
Input
Output

```
1
3 4
1 6 10
```

```
false
```

### Explanation:

No subset of the array adds up to 4.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-11-05T15:57:54.110Z  

```py
class Solution:
    def isSubsetSum(self, n, arr, target):
        # write your code here
        dp=[False]*(target+1)
        dp[0]=True
        for i in range(n):
            for j in range(target,arr[i]-1,-1):
                dp[j]=dp[j] or dp[j-arr[i]]
        return dp[target]
        # def find(ind,arr,target):
        #     if ind==0:
        #         if arr[ind]==target:
        #             return True
        #         else:
        #             return False
        #     if arr[ind]>target:
        #         return False
        #     pick = arr[ind]+find(ind-1,arr,target-arr[ind])
        #     notpick=find(ind-1,arr,target)
        #     return pick or notpick
        # return find(n-1,arr,target)
```

---

[View on CodeChef](https://www.codechef.com/problems/SUBSETTARGET)