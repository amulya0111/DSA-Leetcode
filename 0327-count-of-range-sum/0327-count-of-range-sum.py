class Solution(object):

    def countRangeSum(self, nums, lower, upper):
        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1] + num)
        def mergeSort(left, right):
            if right - left <= 1:
                return 0
            mid = (left + right) // 2
            count = mergeSort(left, mid)
            count += mergeSort(mid, right)
            j = mid
            k = mid
            for i in range(left, mid):
                while j < right and prefix[j] - prefix[i] < lower:
                    j += 1
                while k < right and prefix[k] - prefix[i] <= upper:
                    k += 1
                count += k - j
           # Merge the two sorted halves
            temp = []
            i = left
            j = mid
            while i < mid and j < right:
                if prefix[i] <= prefix[j]:
                    temp.append(prefix[i])
                    i += 1
                else:
                    temp.append(prefix[j])
                    j += 1
            temp.extend(prefix[i:mid])
            temp.extend(prefix[j:right])
            prefix[left:right] = temp
            return count

        return mergeSort(0, len(prefix))