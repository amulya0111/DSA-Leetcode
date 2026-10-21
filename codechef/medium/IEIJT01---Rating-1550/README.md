# IEIJT01 - Rating 1550

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Chef Solves LRU Cache

Chef wants to build a data structure that behaves like a  **Least Recently Used (LRU) cache**  to efficiently manage key–value pairs.

Chef has a  **fixed cache capacity**  and wants to store keys with their values such that  **when the cache exceeds this capacity, the least recently used key is removed**. Chef also wants to retrieve values by keys and update or add new key–value pairs efficiently.

Both retrieval and insertion operations must run in  **average $O(1)$ time**.

### Class Description

Chef will implement a class named  **$LruCache$**.

The class supports the following operations:

- $getValue(cacheKey)$ Returns the value associated with $cacheKey$ if it exists in the cache; otherwise returns $-1$.
- $putValue(cacheKey, cacheValue)$ Inserts or updates the key–value pair in the cache. If the cache is already full, the least recently used key is evicted before inserting the new pair.
## Constraints
- $1 \leq T \leq 10^5$
- $1 \leq cacheCapacity \leq 3000$
- $1 \leq Q \leq 2 \times 10^5$
- $0 \leq cacheKey \leq 10^4$
- $0 \leq cacheValue \leq 10^5$
- The total number of $getValue$ and $putValue$ operations across all test cases does not exceed $2 \times 10^5$.
## Input Format
- The first line contains a single integer $T$ — the number of test cases.
- For each test case: The first line contains an integer $cacheCapacity$ — the capacity of Chef’s LRU cache. The next line contains an integer $Q$ — the number of operations. Each of the next $Q$ lines contains one of the following operations: $get\ cacheKey$ — retrieve the value associated with $cacheKey$. $put\ cacheKey\ cacheValue$ — insert or update the key–value pair.
## Output Format
- For each $get$ operation, print a single line containing: the value associated with $cacheKey$ if it exists, or $-1$ if the key does not exist in the cache.
- print None for $put$ operation.
### Sample 1:
Input
Output

```
1
2
9
put 1 1
put 2 2
get 1
put 3 3
get 2
put 4 4
get 1
get 3
get 4
```

```
None
None
1
None
-1
None
-1
3
4
```

### Explanation:
- put(1, 1) Cache: {1=1} Output: None
- put(2, 2) Cache: {1=1, 2=2} Output: None
- get(1) Returns 1 and marks key 1 as most recently used Cache order: {2=2, 1=1} Output: 1
- put(3, 3) Cache is full ? least recently used key is 2, so it is evicted Cache: {1=1, 3=3} Output: None
- get(2) Key 2 is not present in the cache Output: -1
- put(4, 4) Cache is full ? least recently used key is 1, so it is evicted Cache: {3=3, 4=4} Output: None
- get(1) Key 1 is not present in the cache Output: -1
- get(3) Returns 3 and marks key 3 as most recently used Cache order: {4=4, 3=3} Output: 3
- get(4) Returns 4 Output: 4

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-21T13:54:37.209Z  

```py
class Node:
    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.next = None
        self.prev = None
        
class LruCache:
    def __init__(self, cacheCapacity):
        self.cacheCapacity=cacheCapacity
        self.cache={}
        self.head=Node(0,0)
        self.tail=Node(0,0)
        self.head.next=self.tail
        self.tail.prev=self.head
    def insert(self,node):
        node.next=self.head.next
        self.head.next.prev=node
        self.head.next=node
        node.prev=self.head 
    def remove(self,node):
        nextnode=node.next
        previ=node.prev
        previ.next=nextnode
        nextnode.prev= previ
    def getValue(self, cacheKey: int) -> int:
        if cacheKey not in self.cache:
            return -1
        node=self.cache[cacheKey]
        self.remove(node)
        self.insert(node)
        return node.value
    def putValue(self, cacheKey: int, cacheValue: int) -> None:
        node=Node(cacheKey,cacheValue)
        if cacheKey in self.cache:
            self.remove(self.cache[cacheKey])
            del self.cache[cacheKey]
        self.cache[cacheKey]=node
        self.insert(node)
        if self.cacheCapacity<len(self.cache):
            x=self.tail.prev
            self.remove(x)
            del self.cache[x.key]
        
```

---

[View on CodeChef](https://www.codechef.com/problems/IEIJT01)