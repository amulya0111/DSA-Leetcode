class Solution(object):
    def minSubArrayLen(self, target, nums):
        l = 0
        curr = 0
        ans = float('inf')

        for r in range(len(nums)):
            curr += nums[r]

            while curr >= target:
                ans = min(ans, r - l + 1)
                curr -= nums[l]
                l += 1

        if ans == float('inf'):
            return 0

        return ans