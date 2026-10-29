# Median of Two Sorted Arrays

![Difficulty](https://img.shields.io/badge/Difficulty-Hard-red)

## Problem

Given two sorted arrays `nums1` and `nums2` of size `m` and `n` respectively, return  **the median**  of the two sorted arrays.

The overall run time complexity should be `O(log (m+n))`.

 

 **Example 1:** 

```
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

```

 **Example 2:** 

```
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

```

 

 **Constraints:** 

- nums1.length == m
- nums2.length == n
- 0 <= m <= 1000
- 0 <= n <= 1000
- 1 <= m + n <= 2000
- -106 <= nums1[i], nums2[i] <= 106

## Solution

**Language:** Python  
**Runtime:** 13 ms (beats 6.53%)  
**Memory:** 12.3 MB (beats 89.93%)  
**Submitted:** 2026-10-29T16:52:45.610Z  

```py
class Solution(object):
    def mergesort(self, left, right):
        i = 0
        j = 0
        ans = []

        while i < len(left) and j < len(right):

            if left[i] < right[j]:
                ans.append(left[i])
                i += 1

            elif left[i] > right[j]:
                ans.append(right[j])
                j += 1

            else:
                ans.append(left[i])
                ans.append(right[j])
                i += 1
                j += 1

        ans.extend(left[i:])
        ans.extend(right[j:])

        return ans

    def findMedianSortedArrays(self, nums1, nums2):
        result = self.mergesort(nums1, nums2)

        n = len(result)

        if n % 2 == 0:
            mid = n // 2
            return (result[mid] + result[mid - 1]) / 2.0
        else:
            mid = n // 2
            return result[mid]
        # thats cool!
```

---

[View on LeetCode](https://leetcode.com/problems/median-of-two-sorted-arrays/)