class Solution(object):

    def getMax(self, nums, k):
        stack = []
        remove = len(nums) - k
        for num in nums:
            while remove > 0 and stack and stack[-1] < num:
                stack.pop()
                remove -= 1
            stack.append(num)
        return stack[:k]
        
    def merge(self, a, b):
        i = 0
        j = 0
        result = []
        while i < len(a) and j < len(b):
            if a[i] > b[j]:
                result.append(a[i])
                i += 1
            elif b[j] > a[i]:
                result.append(b[j])
                j += 1
            elif a[i:] > b[j:]:
                result.append(a[i])
                i += 1
            else:
                result.append(b[j])
                j += 1
        result.extend(a[i:])
        result.extend(b[j:])
        return result

    def maxNumber(self, nums1, nums2, k):
        ans = []
        for x in range(max(0, k-len(nums2)), min(k, len(nums1))+1):
            y = k - x
            a = self.getMax(nums1, x)
            b = self.getMax(nums2, y)
            result = self.merge(a, b)
            if result > ans:
                ans = result
        return ans