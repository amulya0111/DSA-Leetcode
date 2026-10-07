# SORTLL012

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Sort a Linked List of 0s, 1s, and 2s

You are given the head of a singly linked list consisting of nodes containing only the integers $0$, $1$, or $2$.
Your task is to sort the linked list such that all $0$s come first, followed by all $1$s, and then all $2$s.

You must perform the sorting  **in-place**  — that is, by rearranging the links between existing nodes, not by creating any new nodes.

## Function Declaration
### Function Name

$sortList$ – This function sorts a linked list containing only $0$s, $1$s, and $2$s.

### Parameters
- $head$ : A pointer to the head of the singly linked list.
### Return Value
- Returns a pointer to the head of the sorted linked list.
- If the list is empty, return $NULL$.
## Constraints
- $1 \leq T \leq 100$
- $0 \leq N \leq 10^5$
- $0 \leq Node.data \leq 2$
- $\text{Sum of } N \text{ over all test cases} \leq 10^5$
### Input Format
- The first line contains an integer $T$ — the number of test cases.
- For each test case: The first line contains an integer $N$ — the number of nodes. The second line contains $N$ space-separated integers representing the node values ($0$, $1$, or $2$).
### Output Format
- For each test case: Print the sorted linked list in a single line (space-separated). If the linked list is empty, print -1.
### Sample 1:
Input
Output

```
3
7
2 1 0 1 2 0 1
0
5
2 2 0 1 0
```

```
0 0 1 1 1 2 2
-1
0 0 1 2 2
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-07T03:17:12.173Z  

```py
def sortList(head):
    # write code here...
    left = temp=head
    if head is None or head.next is None:
        return head 
    zeroh=zerot=oneh=onet=twoh=twot=None
    while temp:
        # first save the upcoming separately
        nextnode=temp.next
        temp.next=None
        # check values and add accordingly 
        if temp.data==0:
            if zeroh is None:
                zeroh=zerot=temp
            else:
                zerot.next=temp
                zerot=zerot.next
        elif temp.data==1:
            if oneh is None:
                oneh=onet=temp
            else:
                onet.next=temp
                onet=onet.next
        elif temp.data==2:
            if twoh is None:
                twoh=twot=temp
            else:
                twot.next=temp
                twot=twot.next
        temp=nextnode
    # finally merge everything(handle None cases for all three, twoh sel handled)
    if zeroh:
        head=zeroh
        if oneh:
            zerot.next=oneh
            zerot=onet
        zerot.next=twoh
    elif oneh:
            head=oneh
            onet.next=twoh
    else:
        head=twoh
        
    return head
                
```

---

[View on CodeChef](https://www.codechef.com/problems/SORTLL012)