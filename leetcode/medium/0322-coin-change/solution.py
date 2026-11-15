class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        n=len(coins)
        # def find(coins,amount,i,dp):
            
        #     if i==len(coins)-1:
        #         if amount%coins[i]==0:
        #             return amount//coins[i]
        #         # else
        #         return float('inf')
            
        #     if coins[i]>amount:
        #         return find(coins,amount,i+1,dp)
        #     if dp[i][amount]!=-1:
        #         return dp[i][amount]
        #     pick=1+find(coins,amount-coins[i],i,dp)
        #     notpick=find(coins,amount,i+1,dp) 
        #     dp[i][amount]=min(pick,notpick)
        #     return min(pick,notpick)
        
        

        # dp=[[-1]*(amount+1) for i in range(n)]
        # ans = find(coins,amount,0,dp) 
        # return ans if ans!=float('inf') else -1

        

        # # TABULATION:(TOP DOWN)
        # dp=[[0]*(amount+1) for i in range(n+1)]
        # for i in range(n-1,-1,-1):
        #     for target in range(1,amount+1):
        #         if i==n-1:
        #             if target%coins[i]==0:
        #                 dp[i][target]=target//coins[i]
        #             else:
        #                 dp[i][target]=float('inf')
        #         else:
        #             pick=float('inf')
        #             if coins[i]<=target:
        #                 pick=1+dp[i][target-coins[i]]
        #             notpick=dp[i+1][target]
        #             dp[i][target]=min(pick,notpick)

        # return dp[0][amount] if dp[0][amount]!=float('inf') else -1
            
        # SINGLE-ARRAY(TOP DOWN)
        prev=[float('inf')]*(amount+1)
        for target in range(amount+1):            
            # we'll store our previous here first , at n-1 i.e the last row which is first processed to become our prev
            if target%coins[n-1]==0:
                prev[target]=target//coins[n-1]
                    
        for i in range(n-2,-1,-1):
            dp=[float('inf')]*(amount+1)
            for target in range(amount+1):
                    pick=float('inf')
                    if coins[i]<=target:
                        pick=1+dp[target-coins[i]]
                    notpick=prev[target]
                    dp[target]=min(pick,notpick)
            prev=dp[:]
        return prev[amount] if prev[amount]!=float('inf') else -1
