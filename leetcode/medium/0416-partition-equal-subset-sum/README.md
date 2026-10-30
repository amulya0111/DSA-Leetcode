# Partition Equal Subset Sum

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given an integer array `nums`, return `true`  *if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or* `false` *otherwise*.

 

 **Example 1:** 

```
Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].

```

 **Example 2:** 

```
Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.

```

 

 **Constraints:** 

- 1 <= nums.length <= 200
- 1 <= nums[i] <= 100

## Solution

**Language:** Python  
**Runtime:** 2468 ms (beats 21.31%)  
**Memory:** 28.2 MB (beats 28.10%)  
**Submitted:** 2026-10-30T13:40:11.788Z  

```py
class Solution(object):
    def canPartition(self, nums):
        k=sum(nums)
        n=len(nums)
        if k%2!=0:
            return False 
        k=k//2
        def checktarget(nums,k):
            # do same as subset sum target, 
            # initialize dp tabulation
            dp=[[False]*(k+1) for i in range(n)]
            # put all target==0 as true 
            for i in range(n):
                dp[i][0]=True
            # if the value is less than target, the column will exist of the value == nums[0] is satisfied!
            if nums[0]<=k:
                dp[0][nums[0]]==True
            # why only nums[0]? as it will be the last element well check 
            # now comes the loop
            for i in range(1,n):
                for target in range(1,k+1):
                    # not take condition , we just pick the previous value from upper column 
                    nottake=dp[i-1][target]
                    # first we will put take as false in case we cant have it(overload) to process it with not take 
                    take = False
                    if nums[i]<=target:
                        take=dp[i-1][target-nums[i]] #checking the remaining target if can be fulfilled or not from previous 
                    dp[i][target]=take or nottake
            return dp[n-1][k]
        return checktarget(nums,k) 

```

---

[View on LeetCode](https://leetcode.com/problems/partition-equal-subset-sum/)