# Celebrity Problem

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Consider a party being organized by some people. A celebrity is a person who is known to all but does not know anyone at the party. 

- A square matrix mat[][] of size n * n is used to represent people at the party such that if an element of row i and column j is set to 1 it means ith person knows jth person.
- You need to return index of the celebrity in the party.
- If the celebrity does not exist, return -1.

 **Note:**  Follow 0-based indexing.

 **Examples:** 

```
Input: mat[][] = [[1, 1, 0],
                 [0, 1, 0],
                 [0, 1, 1]]
Output: 1
Explanation: 0th and 2nd person both know 1st person and 1st person does not know anyone. Therefore, 1 is the celebrity person.
```

```
Input: mat[][] = [[1, 1], 
                 [1, 1]]
Output: -1
Explanation: Since both the people at the party know each other. Hence none of them is a celebrity person.
```

```
Input: mat[][] = [[1]]
Output: 0
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-13T02:02:50.175Z  

```py
class Solution:
    def celebrity(self, mat):
        # create a stack with all indices (celebs)
        stack=[]
        n=len(mat)
        for i in range(n):
            stack.append(i)
        # until s has atleast 1 element (to compare a , b) pop both and check and append accordingly 
        while len(stack)>1:
            a=stack.pop()
            b=stack.pop()
            # if a knows b, a can't be the celeb
            if mat[a][b]==1:
                stack.append(b)
            # else if ==0 b knows a and b cant be the celebrity 
            else:
                stack.append(a)
        # if stack got empty , we dont have a candidate
        if not stack:
            return -1
        # else: check if the last candidate we found is a celebrity or not  
        candidate=stack.pop()
        for i in range(n):
            # ofcourse the candidate knows himself , so check others only 
            if i!=candidate:
                # if celeb knows anyone , return -1
                if mat[candidate][i]== 1 or mat[i][candidate]==0:
                    return -1
                    
        return candidate 
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/the-celebrity-problem/1)