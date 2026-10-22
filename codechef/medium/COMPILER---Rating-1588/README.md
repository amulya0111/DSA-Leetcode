# COMPILER - Rating 1588

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Compilers and Parsers

For an expression to be valid, a “<” symbol must always have a corresponding “>” character somewhere (not necessary immediately) after it. Moreover, each “>” symbol should correspond to exactly one “<” symbol.

So, for instance, the instructions:

```
<>
<>
<><>

```

are all valid. While:

```
>>
><><

```

are not.

Given some expressions which represent some instructions to be analyzed, you should tell the length of the longest  **prefix**  of each of these expressions that is valid, or  **0**  if there's no such a prefix.

### Input

Input will consist of an integer  **T**  denoting the number of test cases to follow.

Then,  **T**  strings follow, each on a single line, representing a possible expression in L++.

### Output

For each expression you should output the length of the longest prefix that is valid or  **0**  if there's no such a prefix.

### Constraints
- 1 ≤ $T$ ≤ 500
- 1 ≤ The length of a single expression ≤ $10^6$
- The total size all the input expressions is no more than $5 * 10^6$
### Sample 1:
Input
Output

```
3
<<>>
><
<>>>
```

```
4
0
2
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-22T01:54:17.340Z  

```py
# cook your dish here
t=int(input())
for _ in range(t):
    stack=[]
    s=input()
    ans=0
    for i in range(len(s)):
        if s[i]=="<":
            stack.append(s[i])
        else:
            if stack:
                stack.pop()
            else:
                break
        if not stack:
            ans=i+1
    print(ans)
```

---

[View on CodeChef](https://www.codechef.com/problems/COMPILER)