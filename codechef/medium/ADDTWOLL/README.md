# ADDTWOLL

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Add Two Numbers (Linked List)

You are given two linked lists that represent two non-negative numbers.
Each number’s digits are stored in  **reverse order**, and every node contains  **a single digit**.

You need to  **add both numbers**  and print the  **resulting linked list**  (also in reverse order).

 **Leading zeros are considered as the nodes because the node's data value can be 0.** 

### Function Declaration
### Function Name

$addTwoNumbers$ – This function adds two non-negative integers represented by two singly linked lists.
Each linked list stores digits in  **reverse order**, where each node contains a single digit (0–9).

The function must compute the sum and return the resulting linked list, also in reverse order.

### Parameters
- $l1$ : A pointer to the head of the first linked list.
- $l2$ : A pointer to the head of the second linked list.
### Return Value
- Returns the head of a new linked list representing the sum of the two numbers.
- Each node contains a single digit.
- If there is a carry after the last digit, an extra node is appended.
## Constraints
- The number of nodes in each linked list is in the range $[1, 100]$.
- $0 \leq \text{Node.data} \leq 9$
### Input Format
- The first line contains an integer $N1$ — the number of nodes in the first linked list.
- The second line contains $N1$ space-separated integers representing the digits of the first number (in reverse order).
- The third line contains an integer $N2$ — the number of nodes in the second linked list.
- The fourth line contains $N2$ space-separated integers representing the digits of the second number (in reverse order).
### Output Format
- Print the resulting linked list representing the sum, with digits separated by spaces.
- The output list must also be in reverse order.
### Sample 1:
Input
Output

```
4
5 9 9 9
3
5 0 0

```

```
0 0 0 0 1

```

### Explanation:

First number $\rightarrow$ 9995
Second number $\rightarrow$ 5 0 0 $\rightarrow$ 005
Sum = 9995 + 5 = 10000
In reverse order $\rightarrow$ `0 0 0 0 1`

### Sample 2:
Input
Output

```
2
9 9
3
1 0 1

```

```
0 0 2

```

### Explanation:

First number $\rightarrow$ 99
Second number $\rightarrow$ 101
Sum = 200
Reverse $\rightarrow$ `0 0 2`

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-10T01:39:45.780Z  

```py
#class Node:
#    def __init__(self, data):
#        self.data = data
#        self.next = None
def addTwoNumbers(l1, l2):
    # write code here...
    ans=Node(0)
    temp=ans
    carry=0
    while l1 or l2 or carry:
        a=l1.data if l1 else 0
        b=l2.data if l2 else 0
        s=a+b+carry
        carry=s//10
        s=s%10
        temp.next=Node(s)
        l1=l1.next if l1 else None
        l2=l2.next if l2 else None
        temp=temp.next
    return ans.next
        
```

---

[View on CodeChef](https://www.codechef.com/problems/ADDTWOLL)