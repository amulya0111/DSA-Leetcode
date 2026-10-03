class Solution(object):
    def merge(self, intervals):
        intervals.sort()

        ans = [intervals[0]]

        for i in range(1, len(intervals)):
            # overlap → merge
            curr=intervals[i]
            if ans[-1][1]>=curr[0]:
                ans[-1][1]=max(ans[-1][1],curr[1])
            # no overlap → append
            else:
                ans.append(curr)
        return ans