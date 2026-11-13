# YHPHV01

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Chef Maximizes Stock Profit - 4

Chef has discovered a fascinating stock market game. There are  **$N$**  days, and on each day  **$i$**, the stock price is given by  **$stockPrices[i]$**. Chef wants to earn as much profit as possible by trading this stock wisely over the given days.

Chef can trade the stock under the following conditions:

- He is allowed to perform at most $maxTransactions$ buy-sell transactions.
- Each transaction consists of buying the stock on one day and selling it on a later day.
- Chef cannot hold more than one stock at a time, which means he must sell the current stock before buying again.

By carefully choosing the days to buy and sell while respecting these rules, Chef wants to determine the  **maximum profit**  he can achieve. Your task is to help Chef calculate this maximum possible profit.

## Function Declaration
- Function Name $calculateMaxProfit$
- Parameters $maxTransactions$— The maximum number of buy-sell transactions Chef is allowed to perform. $stockPrices$ — A list of stock prices, where each element represents the stock price on a particular day.
- Return Value Returns an int representing the maximum profit Chef can achieve. If no profitable transaction is possible, return $0$.
## Constraints
- $1 \le T \le 100000$
- $1 \le N \le 1000$
- $1 \le maxTransactions \le 100$
- $0 \le stockPrices[i] \le 1000$
## Input Format
- The first line contains a single integer $T$ — the number of test cases.
- Each test case consists of: One line containing two integers $N$ and $maxTransactions$ — the number of days and the transaction limit. One line containing $N$ space-separated integers representing $stockPrices$.
## Output Format
- For each test case, print a single integer — the maximum profit Chef can achieve by performing at most $maxTransactions$ transactions.
### Sample 1:
Input
Output

```
3
2 8
1 3 2 8 4 9 0 10
2 5
5 4 3 2 1
2 6
1 2 4 2 5 7

```

```
18
0
8

```

### Explanation:
### Test Case 1 :

Chef has  **$N = 8$**  days and can perform  **at most $2$ transactions**. Stock prices are: `[1, 3, 2, 8, 4, 9, 0, 10]`.

Chef chooses the most profitable transactions:

- Buy at $1$, sell at $9$ -> profit $8$
- Buy at $0$, sell at $10$ -> profit $10$

Total profit =  **$8 + 10 = 18$**.

### Test Case 2 :

Stock prices are: `[5, 4, 3, 2, 1]`.

Prices decrease every day, so there is  **no opportunity to sell at a higher price after buying**.

Hence, Chef cannot make any profit and the answer is  **$0$**.

### Test Case 3 :

Stock prices are: `[1, 2, 4, 2, 5, 7]`, with at most  **$2$ transactions**  allowed.

Chef performs the following transactions:

- Buy at $1$, sell at $4$ -> profit $3$
- Buy at $2$, sell at $7$ -> profit $5$

Total profit =  **$3 + 5 = 8$**.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-11-13T12:26:09.627Z  

```py


def calculateMaxProfit(maxTransactions, stockPrices):
    n=len(stockPrices)
    dp=[0]*(2*maxTransactions+2)
    for i in range(n-1,-1,-1):
        for txn in range(2*maxTransactions-1,-1,-1):
            if txn%2==0:
            # buy
                pick=-stockPrices[i]+dp[txn+1]
                notpick=0+dp[txn]
            else:
                # sell
                pick=stockPrices[i]+dp[txn+1]
                notpick=0+dp[txn]
            dp[txn]=max(pick,notpick)
    return dp[0]
```

---

[View on CodeChef](https://www.codechef.com/problems/YHPHV01)