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