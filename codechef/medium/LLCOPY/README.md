# LLCOPY

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Copy List with Random Pointer

You are given a  **special linked list**  that has two pointers for every node:

- $next$ → points to the next node
- $random$ → can point to any node in the list (or to $NULL$)

Your task is to  **make a deep copy**  of this linked list.

That means you need to create a  **new linked list**  such that:

- Every node in the new list has the same value as the old list.
- The $next$ and $random$ connections are exactly the same as in the original list.
- No new node should point to any node from the original list.

In simple words, you must `clone` the given linked list completely.

## Function Declaration
### Function Name

$copyRandomList$ – This function creates a deep copy of a special linked list where each node contains:

- a $next$ pointer to the next node, and
- a $random$ pointer that may point to any node in the list (or NULL).
### Parameters
- $head$ : A pointer to the head of the original linked list.
### Return Value
- Returns the head of the newly constructed deep-copied linked list.
- If the input list is empty, returns $NULL$.
## Constraints
- $0 \leq N \leq 1000$
- $-10^4 \leq \text{val} \leq 10^4$
- $\texttt{random\_index} = -1$ or $0 \leq \texttt{random\_index} < N$

 **The input and output formats provided below are only for testing with custom inputs. You only need to return the value. Printing is handled automatically.** 

### Input Format
- The first line contains an integer $N$ — the number of nodes in the list.
- The next $N$ lines each contain two space-separated integers: val — the value of the node random_index — the 0-based index of the node that the random pointer points to, or -1 if it is NULL

Nodes appear in index order from `0` to `N−1`.

### Output Format
- Print the deep copied linked list in the format: [[val1, random_index1], [val2, random_index2],..., [valN, random_indexN]]
- If the list is empty, print [].
### Sample 1:
Input
Output

```
3
10 1
20 2
30 0

```

```
[[10,1],[20,2],[30,0]]

```

### Explanation:

The random pointers form a loop:
Node 1 -> Node 2 -> Node 3 -> Node 1

Your deep copy should maintain this cycle, but all nodes must be  **new**.

### Sample 2:
Input
Output

```
0

```

```
[]

```

### Explanation:

The list is empty, so the output is also empty.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-10T04:09:51.232Z  

```py
def copyRandomList(head):

    if head is None:
        return None

    # Step 1: Create copy after every original node
    curr = head

    while curr is not None:
        old_next = curr.next

        copy = Node(curr.val)
        curr.next = copy
        copy.next = old_next

        curr = old_next

    # Step 2: Set random pointers
    curr = head

    while curr is not None:
        copy = curr.next

        if curr.random is not None:
            copy.random = curr.random.next

        curr = copy.next

    # Step 3: Separate the original and copied lists
    curr = head
    new_head = head.next

    while curr is not None:
        copy = curr.next

        curr.next = copy.next

        if copy.next is not None:
            copy.next = copy.next.next

        curr = curr.next

    return new_head
```

---

[View on CodeChef](https://www.codechef.com/problems/LLCOPY)