# YMISN01 - Rating 1050

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Chef Solves Climbing Stairs

Chef has discovered a staircase with $totalSteps$ steps leading to a secret treasure. Chef wants to reach the top by climbing either 1 step or 2 steps at a time.
Chef is curious to know in how many distinct ways he can reach the top of the staircase by combining these moves in different sequences.
Help Chef calculate the total number of unique ways to climb to the top so that he can plan his journey perfectly.

## Function Declaration
### Function Name

$calculateWaysToClimb$ - This function calculates the number of distinct ways to climb a staircase given a total number of steps.

### Parameters
- $totalSteps$: The total number of steps in the staircase that need to be climbed.
### Return Value
- Returns a number representing the total number of unique ways to reach the top of the staircase.
- The output counts all possible sequences of 1-step or 2-step moves that sum to $totalSteps$.
## Constraints
- $1 \leq T \leq 10$
- $1 \leq totalSteps \leq 45$
### Input Format
- The first line contains a single integer $T$ — the number of test cases.
- Each of the next $T$ lines contains a single integer $totalSteps$ — the number of steps in the staircase for that test case.
### Output Format
- For each test case, print a single line containing the number of distinct ways Chef can climb to the top of the staircase.
### Sample 1:
Input
Output

```
4
1
4
10
20
```

```
1
5
89
10946
```

### Explanation:
- t=1: Only 1 step, so 1 way to climb.
- t=4: Ways = 1, 2, 3, 5 for steps 1 to 4; output is 5.
- t=10: Number of ways follows Fibonacci sequence; 10th number is 89.
- t=20: 20th Fibonacci number is 10946, representing ways to climb 20 steps.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-11-03T17:45:19.597Z  

```py
class Solution:
    def calculateWaysToClimb(self, totalSteps: int) -> int:
        # write your code here 
        n=totalSteps
        if n==0 or n==1:
            return 1
        dp=[-1]*(totalSteps+1)
        dp[0]=1
        dp[1]=1
        for i in range(2,totalSteps+1):
            dp[i]=dp[i-1]+dp[i-2]
        return dp[-1]
            
```

---

[View on CodeChef](https://www.codechef.com/problems/YMISN01)