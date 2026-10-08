# ADDONELL

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Linked List Increment

You are given the head of a singly linked list with $N$ nodes, representing a  **positive integer number**.
Each node in the linked list contains a  **single digit (0–9)**, with the  **first node representing the most significant digit**.

Your task is to  **add 1**  to the number represented by the linked list and  **return the updated linked list**.

There will be  **no leading zeroes**  in the given list (except if the number is `0` itself).

## Function Declaration
### Function Name

$addOne$ – This function adds 1 to the integer represented by a singly linked list.
Each node contains a single digit (0–9), where the head node stores the most significant digit.

### Parameters
- $head$ : A pointer to the head of the singly linked list representing the number.
### Return Value
- Returns the head of the linked list after adding 1 to the number.
- If adding 1 results in an extra digit (e.g., 999 → 1000), the function returns the new head containing the additional most significant digit.
## Constraints
- $1 \leq N \leq 10^5$
- $0 \leq \text{Node.data} \leq 9$
### Input Format
- The first line contains an integer $N$ — the number of nodes in the linked list.
- The second line contains $N$ space-separated integers representing the digits of the number (from most significant to least significant).
### Output Format
- Print all digits of the updated number in order, separated by spaces.
### Sample 1:
Input
Output

```
4
5 6 7 8

```

```
5 6 7 9

```

### Explanation:

The linked list represents the number `5678`.
After adding 1 -> `5679`.

### Sample 2:
Input
Output

```
3
2 3 9

```

```
2 4 0

```

### Explanation:

`239 + 1 = 240`.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-08T04:47:07.611Z  

```py
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None


def addOne(head):
    # write code here...
    # lets reverse the LL
    
    
    def reverse(head):
        prev=None
        curr=head 
        while curr:
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
        return prev
    
    # get reversed head 
    curr=reverse(head)
    temp=curr
    s=0
    carry=1
    while temp:
        n=temp.data+carry
        s=n%10
        carry=n//10
        temp.data=s
        temp=temp.next
    curr=reverse(curr)
    if carry>0:
        prev=Node(carry)
        prev.next=curr
        curr=prev
    return curr
        
            
```

---

[View on CodeChef](https://www.codechef.com/problems/ADDONELL)