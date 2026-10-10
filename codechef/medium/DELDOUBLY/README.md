# DELDOUBLY

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Delete All Occurrences of a Key in a Doubly Linked

You are given a  **doubly linked list**  consisting of $N$ nodes and an integer value $X$.
Your task is to  **delete all nodes**  from the linked list whose value is equal to $X$, and then  **return the modified linked list**.
If after deletion the linked list becomes empty, print $-1$.

## Function Declaration
### Function Name

$deleteAllOccurrences$ – This function deletes all nodes with a given value from a doubly linked list.

### Parameters
- $head$ : Pointer to the head of the doubly linked list.
- $X$ : An integer value; all nodes with this value must be deleted.
### Return Value
- Returns the head of the modified doubly linked list.
- Returns $NULL$ if all nodes are deleted (caller prints $-1$).

The input and output formats given below are only if you want to test using custom inputs.

#### Constraints:
- $0 \le N \le 10^{5}$
- $-10^{4} \le \text{Node.data} \le 10^{4}$
- $-10^{4} \le X \le 10^{4}$
### Input Format
- The first line contains an integer $N$ — the number of nodes in the linked list.
- The second line contains $N$ space-separated integers — the elements of the linked list.
- The third line contains an integer $X$ — the value to be deleted from the list.
### Output Format
- Print the elements of the modified linked list after deleting all occurrences of $X$.
- If the list becomes empty, print $-1$.
### Sample 1:
Input
Output

```
6
10 20 30 20 40 20
20

```

```
10 30 40

```

### Explanation:

All nodes with the value `20` are deleted.
The new list becomes: `10 <-> 30 <-> 40`.

### Sample 2:
Input
Output

```
5
5 15 25 35 45
50

```

```
5 15 25 35 45

```

### Explanation:

The value `50` is not present, so the list remains unchanged.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-10T01:50:59.442Z  

```py
#class Node:
#   def __init__(self, data):
#    self.data = data
#    self.next = None
#    self.prev = None



def deleteAllOccurrences(head, X):
    # write code here...
    temp=head 
    while temp:
        if temp.data==X:
            if temp==head:
                head=head.next
            else:
                p=temp.prev
                if temp.next:
                    p.next = temp.next
                    temp.next.prev=p
                else:
                    p.next=None 
        temp=temp.next
    return head 
                    
```

---

[View on CodeChef](https://www.codechef.com/problems/DELDOUBLY)