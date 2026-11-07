# WGBUW01 - Rating 850

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Chef Finds Stock Profit - 1

Chef has discovered the stock market and wants to maximize his profit by buying and selling a stock.
He is given the daily prices of a stock for several days.

Chef can:

- Buy the stock on exactly one day
- Sell the stock on a later day

Chef wants to calculate the maximum profit possible from one buy and one sell operation.
If no profit is possible, the answer should be `0`.

## Function Declaration
- Function Name
- $calculateMaxProfit$
### Parameters
- $\texttt{stockPrices}$ (integer vector): A list of integers where $\texttt{stockPrices}[i]$ represents the stock price on day $i$.
### Return Value
- Returns an integer representing the maximum profit Chef can earn.
- If no profitable transaction is possible, return $0$.
## Constraints
- $1 \le T \le 10^5$ — number of test cases
- $1 \le N \le 10^5$ — number of days
- $0 \le \texttt{stockPrices}[i] \le 10^4$
- The sum of $N$ over all test cases does not exceed $10^5$
## Input Format
- The first line contains an integer $T$ — the number of test cases.
- For each test case: The first line contains an integer $N$ — the number of days. The second line contains $N$ integers — the daily stock prices $\texttt{stockPrices}$.
## Output Format

For each test case, print a single integer — the maximum profit achievable from one buy-sell transaction.
If no profit is possible, print $0$.

### Sample 1:
Input
Output

```
3
4
5 5 5 5
7
1 2 3 4 5 6 7
8
10 7 5 8 11 9 6 15
```

```
0
6
10
```

### Explanation:
- Test Case 1: Stock prices remain constant at 5, so no profitable transaction is possible. Output: 0
- Test Case 2: Stock prices increase daily from 1 to 7. Buying at 1 and selling at 7 yields a profit of 6. Output: 6
- Test Case 3: Buying at price 5 (on day 3) and selling at price 15 (on day 8) gives the maximum profit. Maximum profit = 10

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-11-06T11:46:56.769Z  

```py
def calculateMaxProfit(stockPrices):
    l=0
    maxprofit=0
    if len(stockPrices)==1:
        return 0
    n=len(stockPrices)
    for r in range(1,n):
        if stockPrices[r]<=stockPrices[l]:
            l=r
        else:
            maxprofit=max(maxprofit,stockPrices[r]-stockPrices[l])
    return maxprofit 
```

---

[View on CodeChef](https://www.codechef.com/problems/WGBUW01)