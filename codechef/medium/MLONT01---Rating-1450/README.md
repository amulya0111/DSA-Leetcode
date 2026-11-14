# MLONT01 - Rating 1450

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Chef Calculates Stock Profit - 5

Chef has discovered a new stock trading strategy and wants to maximize his profit from trading a single stock over several days. He is given an array  **$stockPrices$**  where  **$stockPrices[i]$**  represents the stock price on day  **$i$**.

Chef can perform multiple transactions, but he must follow these rules:

- Chef can hold at most one stock at a time, meaning he must sell the currently held stock before buying again.
- After Chef sells a stock on some day, he must take a cooldown of one full day. This means if Chef sells on day $i$, then he cannot buy on day $i+1$, and the earliest next buy is on day $i+2$.

Chef wants to find the maximum profit he can achieve by following these rules. Your task is to help Chef compute this maximum profit.

### Function Declaration
- Function Name: $calculateMaxProfit$
- Parameters: $stockPrices$ (vector<int>) A vector of integers representing stock prices over consecutive days.
- Return Value: Returns an int representing the maximum profit Chef can make. If no profit is possible, return $0$.
## Input Format

The first line contains a single integer  **$T$**  — the number of test cases.

Each test case contains:

- First line: an integer $N$ — the number of days
- Second line: $N$ space-separated integers representing $stockPrices$
## Output Format

For each test case, print a single integer — the  **maximum profit**  Chef can achieve under the cooldown rule.

## Constraints
- $1 \le T \le 10^5$
- $1 \le N \le 2 \times 10^5$
- $0 \le stockPrices[i] \le 1000$
- The sum of $N$ over all test cases does not exceed $2 \times 10^5$
### Sample 1:
Input
Output

```
3
5
1 2 3 0 2
1
1
6
6 1 3 2 4 7
```

```
3
0
6
```

### Explanation:
- Test Case 1 : $stockPrices = [1, 2, 3, 0, 2]$ Buy at $1$ (day 0), sell at $2$ (day 1) -> profit = $1$ Day 2 cooldown Buy at $0$ (day 3), sell at $2$ (day 4) -> profit = $2$

Total profit =  **$1 + 2 = 3$**.

- Test Case 2 :

 **$stockPrices = [1]$** 

Only one day is available, so no valid buy-sell transaction can be completed.

Hence, the output is  **$0$**.

- Test Case 3 : $stockPrices = [6, 1, 3, 2, 4, 7]$ Buy at $1$ (day 1), sell at $7$ (day 5) -> profit = $6$ Trying to sell earlier and rebuy is not better due to cooldown blocking the next buy day.

Hence, the output is  **$6$**.

### Sample 2:
Input
Output

```
2
7
3 8 5 1 7 8 4
4
2 1 4 7
```

```
12
6
```

### Explanation:
- Test Case 1 : $stockPrices = [3, 8, 5, 1, 7, 8, 4]$ Buy at $3$ (day 0), sell at $8$ (day 1) -> profit = $8 - 3 = 5$ Day 2 is cooldown Buy at $1$ (day 3), sell at $8$ (day 5) -> profit = $8 - 1 = 7$

Total profit =  **$5 + 7 = 12$** 

- Test Case 2 : $stockPrices = [2, 1, 4, 7]$ Buy at $1$ (day 1), sell at $7$ (day 3) -> profit = $7 - 1 = 6$ A second transaction is not possible because there are no days left after selling.

Hence, the maximum profit is  **$6$**.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-11-14T15:00:07.536Z  

```py


def calculateMaxProfit(stockPrices):
# TABULATION(ALONG WITH SINGLE)
    prices=stockPrices
    n=len(prices)
    dp=[[0]*2 for i in range(n+1+1)]
    for i in range(n-1,-1,-1):

            pick=-prices[i]+dp[i+1][0]
            notpick=0+dp[i+1][1]
            dp[i][1]=max(pick,notpick)
            
            pick=prices[i]+dp[i+2][1]
            notpick=0+dp[i+1][0]        
            dp[i][0]=max(pick,notpick)
    return dp[0][1]



```

---

[View on CodeChef](https://www.codechef.com/problems/MLONT01)