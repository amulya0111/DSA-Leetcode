# VYISQ01 - Rating 1450

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Chef Verifies Equal Subset Sum

Chef has found a list of positive integers and wants to split this list into two subsets such that the sum of the elements in both subsets is exactly equal. Chef wonders if it is possible to partition the given list into two parts with equal sum. Help Chef determine whether such a partition exists.

Chef needs a function that, given an integer list, returns `true` if it can be divided into two subsets with equal sums, and `false` otherwise.

## Function Declaration
### Function Name

$canPartitionEqualSubset$ - Determines if the given list of integers can be partitioned into two subsets with equal sums.

### Parameters
- $integerVector numbers$ (vector&): A vector of positive integers representing the input set.
### Return Value
- Returns a boolean ($bool$) value.
- $true$ if the input list can be divided into two subsets with equal sum; otherwise, $false$.
## Constraints
- $1 \leq \text{T} \leq 10$
- $1 \leq \text{numbersCount} \leq 200$
- $1 \leq \text{numbers}[i] \leq 100$
## Input Format
- The first line contains a single integer $T$ — the number of test cases.
- For each test case: The first line contains an integer $N$ — the size of Chef's array. The second line contains $N$ space-separated integers representing Chef's array.
## Output Format

For each test case, print a single line containing `true` if Chef can partition the array into two subsets with equal sums, or `false` otherwise. Help Chef print the correct answer!

### Sample 1:
Input
Output

```
3
4
2 2 3 5
5
1 2 3 4 5
6
1 1 1 1 1 1
```

```
false
false
true
```

### Explanation:
- Test Case 1 : Array: [2, 2, 3, 5] Total sum = 2 + 2 + 3 + 5 = 12 To split into two equal subsets, each subset must have sum = 12 / 2 = 6. Possible subset sums from the array: 2 + 2 + 3 = 7 5 + 2 = 7 3 + 2 = 5 No subset adds up to exactly 6, so equal partition is not possible. Hence, the output is false.
- Test Case 2 Array: [1, 2, 3, 4, 5] Total sum = 1 + 2 + 3 + 4 + 5 = 15 Since the total sum is odd, it cannot be divided into two equal integer parts. Hence, the output is false.
- Test Case 3 Array: [1, 1, 1, 1, 1, 1] Total sum = 6 Each subset must have sum = 6 / 2 = 3. One valid partition is: Subset 1: [1, 1, 1] -> sum = 3 Subset 2: [1, 1, 1] -> sum = 3 Hence, the output is true.
### Sample 2:
Input
Output

```
2
8
1 1 1 1 1 1 1 7
5
2 4 6 8 10
```

```
true
false
```

### Explanation:
- Test Case 1 : Array: [1, 1, 1, 1, 1, 1, 1, 7] Total sum = 1+1+1+1+1+1+1+7 = 14 Each subset must have sum = 14 / 2 = 7. Chef can form sum 7 in two ways: Subset 1: [7] -> sum = 7 Subset 2: [1, 1, 1, 1, 1, 1, 1] -> sum = 7 Hence, the output is true.
- Test Case 2 Array: [2, 4, 6, 8, 10] Total sum = 2 + 4 + 6 + 8 + 10 = 30 Each subset must have sum = 30 / 2 = 15. Possible subset sums: 10 + 4 = 14 8 + 6 = 14 8 + 4 + 2 = 14 10 + 6 = 16 No combination gives exactly 15, so equal partition is not possible. Hence, the output is false.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-11-09T14:53:55.724Z  

```py
def canPartitionEqualSubset(numbers):
    total=sum(numbers)
    if total%2!=0:
        return False
    target=total//2
    n=len(numbers)
    dp=[False]*(target+1)
    dp[0]=True
    for i in range(n):
        for j in range(target,numbers[i]-1,-1):
            dp[j]= dp[j] or dp[j-numbers[i]]
    return dp[target]

```

---

[View on CodeChef](https://www.codechef.com/problems/VYISQ01)