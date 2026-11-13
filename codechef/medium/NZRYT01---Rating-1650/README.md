# NZRYT01 - Rating 1650

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Chef Finds Stock Profit - 3

Chef has been observing the stock market closely and wants to maximize his profit by trading a single stock. He is given the prices of the stock over several days.

Chef is allowed to complete  **at most two transactions**  to earn profit. A transaction consists of  **buying**  the stock on one day and  **selling**  it on a later day. Chef must follow a strict rule:  **he cannot hold more than one stock at a time**, which means he must sell the current stock before buying again.

Chef wants to determine the  **maximum profit**  he can achieve under these conditions.

Your task is to help Chef calculate the  **highest possible profit**  by performing at most two transactions.

## Function Declaration
- Function Name $calculateMaxProfit$
- Parameters $stockPrices$ — An array of integers representing the price of the stock on each day.
- Return Value Returns an int representing the maximum profit Chef can achieve. If no profit is possible, return $0$.
## Constraints
- $1 \le T \le 10^5$
- $1 \le |stockPrices| \le 10^5$
- $0 \le stockPrices[i] \le 10^5$
## Input Format
- The first line contains a single integer $T$ — the number of test cases.
- Each test case consists of: A line containing an integer $N$ — the number of days. A line containing $N$ space-separated integers representing $stockPrices$.
## Output Format
- For each test case, print a single integer — the maximum profit Chef can achieve by performing at most two transactions.
- If no profit can be made, print $0$.
### Sample 1:
Input
Output

```
3
8
1 3 2 8 4 9 0 10
5
5 4 3 2 1
6
1 2 4 2 5 7
```

```
18
0
8
```

### Explanation:
- Test Case 1 : For $stockPrices = [1, 3, 2, 8, 4, 9, 0, 10]$, Chef can perform at most two transactions. First transaction: Buy at $1$, sell at $9$ Profit = $9 - 1 = 8$ Second transaction: Buy at $0$, sell at $10$ Profit = $10 - 0 = 10$ Total profit = $8 + 10 = 18$
- Test Case 2 : For $stockPrices = [5, 4, 3, 2, 1]$, stock prices keep decreasing every day. Since there is no opportunity to sell at a higher price after buying, Chef cannot make any profit. Hence, the maximum profit is $0$.
- Test Case 3 : For $stockPrices = [1, 2, 4, 2, 5, 7]$, Chef chooses the best two transactions: First transaction: Buy at $1$, sell at $4$ Profit = $4 - 1 = 3$ Second transaction: Buy at $2$, sell at $7$ Profit = $7 - 2 = 5$ Total profit = $3 + 5 = 8$

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-11-13T12:51:36.501Z  

```py
def calculate_max_profit(stockPrices):
    # buy1=buy2=-float('inf')
    # sell1=sell2=0
    # for Price in stockPrices:
    #     b1=buy1
    #     b2=buy2
    #     s1=sell1
    #     s2=sell2
    #     buy1=max(buy1,-Price)
    #     sell1=max(sell1,buy1+Price)
    #     buy2=max(buy2,sell1-Price)
    #     sell2=max(sell2,buy2+Price)
    # return sell2
    # # 
    n=len(stockPrices)
    dp=[0]*(5)
    for i in range(n-1,-1,-1):
        for txn in range(3,-1,-1):
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

[View on CodeChef](https://www.codechef.com/problems/NZRYT01)