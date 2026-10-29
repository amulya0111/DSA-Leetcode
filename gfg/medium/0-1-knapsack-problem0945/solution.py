class Solution:
    def knapsack(self, W: int, val: list[int], wt: list[int]) -> int:
        dp=[0]*(W+1)
        for i in range(len(wt)):
            for w in range(W,wt[i]-1,-1):
                pick=val[i]+dp[w-wt[i]]
                not_pick=dp[w]
                dp[w]=max(pick,not_pick)
        return dp[W]