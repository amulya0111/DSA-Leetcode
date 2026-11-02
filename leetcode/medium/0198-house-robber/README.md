# House Robber

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and  **it will automatically contact the police if two adjacent houses were broken into on the same night**.

Given an integer array `nums` representing the amount of money of each house, return  *the maximum amount of money you can rob tonight  **without alerting the police***.

 

 **Example 1:** 

```
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

```

 **Example 2:** 

```
Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.

```

 

 **Constraints:** 

- 1 <= nums.length <= 100
- 0 <= nums[i] <= 400

## Solution

**Language:** Python  
**Runtime:** 0 ms (beats 100.00%)  
**Memory:** 12.2 MB (beats 75.88%)  
**Submitted:** 2026-11-02T18:13:57.397Z  

```py
class Solution(object):
    def rob(self, nums):
        if len(nums)<=2:
            return max(nums)
        dp=[0]*len(nums)
        dp[0]=nums[0]
        dp[1]=max(nums[0],nums[1]) #As we can take farther value 0 for 2nd index 
        for i in range(2,len(nums)):
            pick=max(dp[i-2]+nums[i],nums[i])
            notpick=dp[i-1]
            dp[i]=max(pick,notpick)
        return dp[len(nums)-1]
```

---

[View on LeetCode](https://leetcode.com/problems/house-robber/)