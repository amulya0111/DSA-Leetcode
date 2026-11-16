# DORKL01 - Rating 1450

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Chef Solves Coin Change II

Chef has a collection of coins, each with a distinct denomination $coinDenominations$, and Chef wants to find out how many different ways there are to make up a given total amount using these coins $targetAmount$.
Chef can use as many coins of each denomination as needed, including none. Help Chef by calculating the number of unique combinations of coins that sum exactly to the target amount.
If it is impossible to form the target amount using the given coins, Chef should know that the answer is zero.

## Function Declaration
### Function Name

$countCoinCombinations$ - This function calculates the number of distinct ways to make up a given $targetAmount$ using the specified $coinDenominations$.

### Parameters
- $targetAmount$ : The total amount of money to form using coins. It is a non-negative integer.
- $coinDenominations$: A list of distinct positive integers representing the available coin denominations.
### Return Value
- Returns an integer representing the total number of unique combinations to form targetAmount using any number of coins from $coinDenominations$.
- The output is a non-negative integer indicating the count of possible combinations.
## Constraints
- $1 \leq \text{length of } coinDenominations \leq 300$
- $1 \leq coinDenominations[i] \leq 5000$
- All values in coinDenominations are unique.
- $0 \leq targetAmount \leq 5000$
### Input Format
- The first line contains a single integer $T$ — the number of test cases.
- Each test case consists of two lines: First line containing a value $targetAmount$ — the total amount Chef wants to form. Second line containing distinct integers enclosed in [ and ] separated by, representing the $coinDenominations$.
### Output Format
- For each test case, print a single line containing the number of unique combinations Chef can use to form the $targetAmount$.
- If Chef cannot form the amount using the given coins, print $0$.
### Sample 1:
Input
Output

```
2
5
[1, 2, 5]
3
[2]

```

```
4
0
```

### Explanation:
### Test Case 1

 **Coin Denominations:**  `[1, 2, 5]`  **Target Amount:**  `5`

Chef wants to find the number of  **unique combinations**  of these coins that sum to  **5**. Coins can be used  **any number of times**, and the  **order of coins does not matter**.

#### Valid combinations:
- 1 + 1 + 1 + 1 + 1
- 1 + 1 + 1 + 2
- 1 + 2 + 2
- 5

Total number of unique combinations =  **4** 

### Test Case 2

 **Coin Denominations:**  `[2]`  **Target Amount:**  `3`

Chef only has a coin of value `2`.

- Using any number of 2s will always produce an even sum
- The target amount 3 is odd

It is  **impossible**  to form `3` using only coin `2`

Total number of combinations =  **0** 

### Sample 2:
Input
Output

```
2
10
[10]
5
[5]

```

```
1
1
```

### Explanation:
### Test Case 1

 **Coin Denominations:**  `[10]`  **Target Amount:**  `10`

Chef has only one coin type with value `10`.

#### Valid combination:
- 10

Total number of combinations =  **1** 

### Test Case 2

 **Coin Denominations:**  `[5]`  **Target Amount:**  `5`

Chef has only one coin type with value `5`.

#### Valid combination:
- 5

Total number of combinations =  **1**

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-11-16T05:17:43.698Z  

```py
def countCoinCombinations(targetAmount, coinDenominations):
    amount=targetAmount
    coins=coinDenominations
    n=len(coinDenominations)
    prev=[0]*(amount+1)
    prev[0]=1
    for i in range(n-1,-1,-1):
        dp=[0]*(amount+1)
        dp[0]=1
        for target in range(amount+1):
            pick=0
            if coins[i]<=target:
                pick=dp[target-coins[i]]
            notpick=prev[target]
            dp[target]=pick+notpick
        prev=dp[:]

    return prev[amount] 
    

```

---

[View on CodeChef](https://www.codechef.com/problems/DORKL01)