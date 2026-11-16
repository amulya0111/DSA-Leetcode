class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        n=len(coins)
        # dp=[[-1]*(amount+1) for i in range(n)]
        # def count(i,target,coins,dp):
        #     if target==0:
        #         return 1
        #     if i==len(coins):
        #         return 0
        #     if coins[i]>target:
        #         return count(i+1,target,coins,dp)
        #     if dp[i][target]!=-1:
        #         return dp[i][target]
        #     pick=0+count(i,target-coins[i],coins,dp)
        #     notpick=0+count(i+1,target,coins,dp)
        #     return pick+notpick
        # return count(0,amount,coins,dp)

        # dp=[[0]*(amount+1) for i in range(n+1)]
        # for i in range(n+1):
        #     dp[i][0]=1
        # for i in range(n-1,-1,-1):
        #     for target in range(amount+1):
        #         pick=0
        #         if coins[i]<=target:
        #             pick=dp[i][target-coins[i]]
        #         notpick=dp[i+1][target]
        #         dp[i][target]=pick+notpick
        # return dp[0][amount]

        prev=[0]*(amount+1)
        prev[0]=1
        for i in range(n-1,-1,-1):
            dp=[0]*(amount+1)
            dp[0]=1
            for target in range(amount+1):
                pick=0
                if coins[i]<=target:
                    pick=dp[target-coins[i]]
                notpick=prev[target]
                dp[target]=pick+notpick
            prev=dp[:]

        return prev[amount]             