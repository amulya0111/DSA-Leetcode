class Solution(object):

    def merge(self, left, right, result):
        i = 0
        j = 0
        ans = []
        rightSmaller = 0
        while i < len(left) and j < len(right):
            if left[i][0] <= right[j][0]:
                result[left[i][1]] += rightSmaller
                ans.append(left[i])
                i += 1
            else:
                ans.append(right[j])
                rightSmaller += 1
                j += 1
        while i < len(left):
            result[left[i][1]] += rightSmaller
            ans.append(left[i])
            i += 1
        ans.extend(right[j:])
        return ans

    def sort(self, arr, result):
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left = self.sort(arr[:mid], result)
        right = self.sort(arr[mid:], result)
        return self.merge(left, right, result)

    def countSmaller(self, nums):
        result = [0] * len(nums)
        arr = [(nums[i], i) for i in range(len(nums))]
        self.sort(arr, result)
        return result
