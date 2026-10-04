class Solution(object):
    def insert(self, intervals, newInterval):
        ans = []
        i = 0
        n = len(intervals)

        # intervals before newInterval
        while i < n and intervals[i][1] < newInterval[0]:
            ans.append(intervals[i])
            i += 1

        # merge overlapping intervals, pehle naye interval k0 banao loop me phir inseet karna  
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1

        ans.append(newInterval)

        # intervals after newInterval
        while i < n:
            ans.append(intervals[i])
            i += 1

        return ans