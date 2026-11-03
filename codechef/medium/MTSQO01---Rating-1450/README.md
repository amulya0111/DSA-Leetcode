# MTSQO01 - Rating 1450

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Chef robs House II

Chef is planning a heist on a circular street where houses are arranged in a circle. Each house contains some amount of money, but adjacent houses have connected security systems.
If Chef robs two adjacent houses on the same night, the alarm will trigger, and the police will be alerted. Chef wants to maximize the amount of money stolen without triggering the alarm.
Help Chef determine the maximum amount of money that can be robbed tonight under these strict security constraints.

## Function Declaration
### Function Name

$calculateMaxRobAmount$ - This function calculates the maximum amount of money that Chef can rob from a circular list of houses without robbing two adjacent houses.

### Parameters
- $houseMoneyList$ : A reference to a vector of integers representing the amount of money available in each house.
- Each element in $houseMoneyList$ is a non-negative integer indicating the money in that house.
### Return Value
- Returns a number representing the maximum sum of money that can be robbed without triggering alarms.
- The output is a single integer value indicating the optimal robbery amount.
## Constraints
- $1 \leq number of houses \leq 100$
- $0 \leq houseMoneyList[i] \leq 1000$

 **The input and output formats given below are only if you want to test using custom inputs.** 

### Input Format
- The first line contains a single integer $T$ — the number of test cases.
- Each test case contains: Next line contains comma separated integers in [] representing the amount of money in each house, i.e., the $houseMoneyList$.
### Output Format
- For each test case, print a single line containing the maximum amount of money Chef can rob without alerting the police.
### Sample 1:
Input
Output

```
3
[2, 3, 2]
[1, 2, 3, 1]
[1, 2, 3]
```

```
3
4
3
```

### Explanation:
- For [2, 3, 2], robbing house 2 (3) yields the max amount without alerting neighbors, so output is 3.
- For [1, 2, 3, 1], rob houses 2 (2) and 4 (1) or houses 1 (1) and 3 (3), max sum is 4.
- For [1, 2, 3], rob house 3 (3) for the maximum amount since first and last are adjacent.
### Sample 2:
Input
Output

```
4
[500]
[1000, 1000]
[0, 0, 0]
[10, 20, 30, 40, 50, 60, 70]
```

```
500
1000
0
150
```

### Explanation:
- t=1: Only one house with 500, rob it for 500.
- t=2: Two houses with 1000 each, rob either one for 1000.
- t=3: All houses have 0, maximum loot is 0.
- t=4: Rob houses 2, 4, 6 (20+40+60=120) or 3, 5, 7 (30+50+70=150), max is 150.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-11-03T17:39:05.536Z  

```py
def calculateMaxRobAmount(houseMoneyList):
    # write your code here 
    nums=houseMoneyList
    if len(nums)<=3:
        return max(nums)
    def robbery(nums):
        dp=[0]*len(nums)
        dp[0]=nums[0]
        dp[1]=max(nums[0],nums[1])
        for i in range(2,len(nums)):
            dp[i]=max(dp[i-2]+nums[i],nums[i-1])
        return dp[-1]
    dp1=robbery(nums[1:])
    dp2=robbery(nums[:-1])
    return max(dp1,dp2)
```

---

[View on CodeChef](https://www.codechef.com/problems/MTSQO01)