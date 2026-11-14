# JKPLU01

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Chef Calculates Stock Profit - 6

Chef has discovered a new way to maximize his earnings by trading stocks. He is given a list of daily stock prices and wants to earn the maximum possible profit.

Chef can buy and sell the stock multiple times, but there is an important condition:  **every completed transaction (one buy followed by one sell) incurs a fixed transaction fee**. Chef cannot hold more than one stock at a time, so he must sell the current stock before buying again.

Chef wants to determine the  **maximum profit**  he can achieve after accounting for the transaction fees.

Your task is to help Chef calculate the  **maximum achievable profit**.

## Function Declaration
- Function Name $calculateMaxProfit$
- Parameters $stockPrices$ — A list of integers representing the stock price on each day. $transactionFee$ — The fee charged for each completed transaction.
- Return Value Returns an int representing the maximum profit Chef can obtain after paying all transaction fees.
## Constraints
- $1 \le T \le 10^5$
- $1 \le N \le 5 \times 10^4$
- $1 \le stockPrices[i] \le 5 \times 10^4$
- $0 \le transactionFee \le 5 \times 10^4$
## Input Format
- The first line contains a single integer $T$ — the number of test cases.
- Each test case consists of: First line containing an integer $N$ — the number of days. Second line containing $N$ space-separated integers representing $stockPrices$. Third line containing an integer $transactionFee$ — the transaction fee.
## Output Format
- For each test case, print a single integer — the maximum profit Chef can make after paying the transaction fees.
### Sample 1:
Input
Output

```
2
6
1 3 2 8 4 9
2
6
1 3 7 5 10 3
3
```

```
8
6
```

### Explanation:
- Test Case 1 : For $stockPrices = [1, 3, 2, 8, 4, 9]$ and $transactionFee = 2$, Chef performs the following transactions: Buy at $1$, sell at $8$ Profit = $8 - 1 - 2 = 5$ Buy at $4$, sell at $9$ Profit = $9 - 4 - 2 = 3$ The total profit is: $5 + 3 = 8$ Hence, the maximum profit is $8$.
- Test Case 2 : For $stockPrices = [1, 3, 7, 5, 10, 3]$ and $transactionFee = 3$, Chef chooses the optimal strategy: Buy at $1$, sell at $10$ Profit = $10 - 1 - 3 = 6$ Any attempt to split into multiple transactions would reduce the total profit due to additional transaction fees. Hence, the maximum profit is $6$.
### Sample 2:
Input
Output

```
1
5
2 5 1 6 4
2
```

```
4
```

### Explanation:

stockPrices = [2, 5, 1, 6, 4] and transactionFee = 2, Chef performs the following transactions:

Buy at 2, sell at 5 Profit = 5 - 2 - 2 = 1

Buy at 1, sell at 6 Profit = 6 - 1 - 2 = 3

Any further transaction is not profitable due to the transaction fee.

The total profit is: 1 + 3 = 4

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-11-14T15:10:06.888Z  

```py
def calculateMaxProfit(stockPrices: list[int], transactionFee: int) -> int:
    n=len(stockPrices)
    dp=[0]*2
    for i in range(n-1,-1,-1):
        dp[1]=max(-stockPrices[i]+dp[0],0+dp[1])
        dp[0]=max(stockPrices[i]+dp[1]-transactionFee,0+dp[0])
    return dp[1]
```

---

[View on CodeChef](https://www.codechef.com/problems/JKPLU01)