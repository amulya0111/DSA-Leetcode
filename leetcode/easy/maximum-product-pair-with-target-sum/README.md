# Q1. Maximum Product Pair With Target Sum

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

You are given an integer array `nums` and an integer `target`.

A pair of  **distinct**  indices `(i, j)` is  **valid**  if:

- nums[i] + nums[j] == target
- nums[i] > nums[j]

Return a  **valid**  pair `[i, j]` whose  **product**  `nums[i] * nums[j]` is  **maximum**  among all valid pairs. If no valid pair exists, return `[-1, -1]`.

If multiple valid pairs achieve the  **maximum**  product, you may return  **any**  of them.

 

 **Example 1:** 

 **Input:**  nums = [1,2,3,4], target = 5

 **Output:**  [2,1]

 **Explanation:** 

There are 2 valid pairs:

No.	`(i, j)`	`nums[i]`	`nums[j]`	Sum	Product
1	(3, 0)	4	1	5	4
2	(2, 1)	3	2	5	6

Both pairs sum to 5 and satisfy `nums[i] > nums[j]`. The second pair has the larger product, `3 * 2 = 6`, so the answer is `[2, 1]`.

 **Example 2:** 

 **Input:**  nums = [-3,-1,4,2], target = 1

 **Output:**  [3,1]

 **Explanation:** 

There are 2 valid pairs:

No.	`(i, j)`	`nums[i]`	`nums[j]`	Sum	Product
1	(2, 0)	4	-3	1	-12
2	(3, 1)	2	-1	1	-2

Since `-2 > -12`, the pair at indices `(3, 1)` is chosen and the answer is `[3, 1]`.

 **Example 3:** 

 **Input:**  nums = [3,3,5], target = 6

 **Output:**  [-1,-1]

 **Explanation:** 

 **​​​​​​​** No valid pair exists, since `nums[0]` and `nums[1]` sum to 6 but are equal.

 

 **Constraints:** 

- 2 <= nums.length <= 100
- -100 <= nums[i], target <= 100​​​​​​​

## Solution

**Language:** Python  
**Runtime:** 0 ms  
**Memory:** 12.5 MB  
**Submitted:** 2026-10-10T15:33:18.559Z  

```py
class Solution(object):
    def maxProductPair(self, nums, target):
        l=0        
        r=len(nums)-1
        result=[-1,-1]
        ans=float("-inf")
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    if ans<nums[i]*nums[j] and nums[i]!=nums[j]:
                        ans=nums[i]*nums[j]
                        result=[i,j] if nums[i]>nums[j] else [j,i]
                        
            
        return result
```

---

[View on LeetCode](https://leetcode.com/problems/maximum-product-pair-with-target-sum/)