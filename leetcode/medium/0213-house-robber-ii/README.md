# House Robber II

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are  **arranged in a circle.**  That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and  **it will automatically contact the police if two adjacent houses were broken into on the same night**.

Given an integer array `nums` representing the amount of money of each house, return  *the maximum amount of money you can rob tonight  **without alerting the police***.

 

 **Example 1:** 

```
Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.

```

 **Example 2:** 

```
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

```

 **Example 3:** 

```
Input: nums = [1,2,3]
Output: 3

```

 

 **Constraints:** 

- 1 <= nums.length <= 100
- 0 <= nums[i] <= 1000

## Solution

**Language:** Python  
**Runtime:** 0 ms (beats 100.00%)  
**Memory:** 11.9 MB (beats 99.07%)  
**Submitted:** 2026-11-03T17:32:16.045Z  

```py
class Solution(object):
    def rob(self, nums):
        if len(nums)<=3:
            return max(nums)
        def house(nums):
            dp=[0]*len(nums)
            dp[0]+=nums[0]
            dp[1]+=max(nums[0],nums[1])

            for i in range(2,len(nums)):
                dp[i]=max(dp[i-2]+nums[i],dp[i-1]) #OOOHHHH
            return dp[-1]
        dp1=house(nums[:-1])
        dp2=house(nums[1:])
        return max(dp1,dp2)

```

---

[View on LeetCode](https://leetcode.com/problems/house-robber-ii/)